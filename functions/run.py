import subprocess
import sys
from pathlib import Path


def run_python_file(working_directory, file_path, args=[]):
    working_directory = Path(working_directory).resolve()
    fp = working_directory.joinpath(file_path).resolve()

    if not fp.is_relative_to(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not fp.exists():
        return f'Error: File "{file_path}" not found.'
    if fp.suffix != ".py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            [sys.executable, str(fp)] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
            cwd=working_directory,
            text=True,
        )
        output = ""
        if result.returncode:
            output += f"Process exited with code {result.returncode}\n"
        if result.stdout:
            output += f"STDOUT:\n{result.stdout}\n"
        if result.stderr:
            output += f"STDERR:\n{result.stderr}\n"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
