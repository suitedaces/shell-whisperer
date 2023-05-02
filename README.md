# 🔮 Shell Whisperer 🔮

Shell Whisperer is a command-line productivity tool for Python developers that generates CLI (Command Line Interface) commands based on natural language input. Powered by OpenAI's GPT-3.5-turbo language model, Shell Whisperer can understand a wide range of tasks described in plain English and provide the corresponding shell commands. Optionally, it can also provide explanations of how the generated commands work.

## Features

- Generate shell commands based on natural language descriptions.
- Supports a variety of tasks, from file management to system administration.
- Option to provide explanations for the generated commands.
- User-friendly (🧢) command-line interface.

## Installation
To install Shell Whisperer, you can use pip, the Python package manager. We recommend installing Shell Whisperer in a virtual environment to isolate it from your system Python environment.

Creating a Virtual Environment
To create a virtual environment, follow these steps:

   ```shell
   # Navigate to your desired directory
  cd /path/to/directory

  # Create a virtual environment named 'venv'
  python3 -m venv venv

  # Activate the virtual environment
  source venv/bin/activate  # On macOS and Linux
  venv\Scripts\activate     # On Windows
   ```

## Installing Shell Whisperer
With the virtual environment activated, you can install Shell Whisperer from PyPI using the following command:

   ```shell
    pip install shell-whisperer
   ```
This will download and install Shell Whisperer and its dependencies.

### Usage
Once installed, you can use the whisperer command (or the entry point you defined) to interact with Shell Whisperer. Here's an example of how to use the tool:

### Provide whisperer with your OpenAI keys
   ```shell
   whisperer configure 
   ```
   Output: 
   Enter your OpenAI key: <enter_your_OpenAI_key>

### After configuration, request Shell Whisperer to generate a command
   ```shell
   whisperer request "list all files in the current directory"
   ```


### Request an explanation of the generated command
   ```shell
   whisperer request "list all files in the current directory" --explain
   ```


## Contributing
I welcome contributions to Shell Whisperer! If you encounter any issues or have feature requests, please feel free to open an issue on the project's repository.

## License
Shell Whisperer is released under the MIT License.


