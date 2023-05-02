import json
import os
import subprocess
from pathlib import Path

import pyperclip
import typer
from rich import print
from rich.prompt import Confirm, Prompt

from whisperer.gpt_whisperer import GPTWhisperer
from whisperer.utils import get_os_info

APP_NAME = ".whisperer"
app = typer.Typer()


@app.command()
def configure():
    """Configure the Shell Whisperer with your OpenAI API key."""
    api_key = Prompt.ask("Enter your OpenAI API key")

    os_family, os_fullname = get_os_info()
    if os_family:
        if not Confirm.ask(f"Is your operating system {os_fullname}?"):
            os_fullname = Prompt.ask("Enter your operating system and version (e.g., macOS 13.1)")
    else:
        os_fullname = Prompt.ask("Enter your operating system and version (e.g., macOS 13.1)")

    shell = os.environ.get("SHELL", "").split("/")[-1] or Prompt.ask("Enter your shell (e.g., bash, zsh)")

    config = {
        "backend": "openai-gpt-3.5-turbo",
        "openai_api_key": api_key,
        "os": os_family,
        "os_fullname": os_fullname,
        "shell": shell,
    }

    app_dir = typer.get_app_dir(APP_NAME)
    config_path = Path(app_dir) / "config.json"
    print("Saving the following configuration...")
    print(config)

    config_path.parent.mkdir(parents=True, exist_ok=True)

    if config_path.exists():
        overwrite = Confirm.ask(
            "A configuration file already exists. Do you want to overwrite it?"
        )
        if not overwrite:
            print("Did not overwrite the file.")
            return

    with open(config_path, "w") as f:
        json.dump(config, f)

    print(f"[bold green]Configuration saved at {config_path}[/bold green]")


@app.command()
def request(
        task: str = typer.Argument(..., help="What task do you want to accomplish?"),
        explain: bool = False,
):
    """Ask the whisperer to run the command you desire."""
    app_dir = typer.get_app_dir(APP_NAME)
    config_path = Path(app_dir) / "config.json"

    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[red]Error: Configuration not found or invalid. Please run the 'configure' command first.[/red]")
        return

    whisperer = GPTWhisperer(
        api_key=config["openai_api_key"],
        os_fullname=config["os_fullname"],
        shell=config["shell"],
    )
    try:
        command, description = whisperer.request(task, explain)
    except Exception as e:
        print(f"[red]Error: {e}[/red]")
        return

    print(f"[bold]Command:[/bold] [orange]{command}[/orange]")
    if description:
        print(f"[bold]Description:[/bold] {description}")

    if config["os"] == "Windows" and config["shell"] == "powershell":
        pyperclip.copy(command)
        print("[green]Command copied to clipboard.[/green]")
    else:
        execute = Confirm.ask("Do you want to execute the command?")
        if execute:
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError:
                print("[red]Error: The command failed to execute.[/red]")


if __name__ == "__main__":
    app()
