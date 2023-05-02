import platform

def get_os_info():
    """Retrieve information about the operating system."""
    oper_sys = platform.system()
    if oper_sys == "Windows" or oper_sys == "Darwin":
        oper_sys = "MacOS" if oper_sys == "Darwin" else "Windows"
        return (oper_sys, platform.platform(aliased=True, terse=True))
    if oper_sys == "Linux":
        return (oper_sys, platform.freedesktop_os_release()["PRETTY_NAME"])
    return (None, None)