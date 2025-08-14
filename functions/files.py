from pathlib import Path

import config


def get_files_info(working_directory, directory=".") -> str:
    working_directory = Path(working_directory).resolve()
    directory = working_directory.joinpath(directory).resolve()

    if not directory.is_relative_to(working_directory):
        return f'Error: Cannot list "{str(object=directory)}" as it is outside the permitted working directory'
    if not directory.is_dir():
        return f'Error: "{str(directory)}" is not a directory'
    if not directory.exists():
        return f'Error: "{str(directory)}" not found'

    try:
        output = ""
        for path in directory.rglob("*"):
            output += f" - {path.name}: file_size={path.stat().st_size} bytes, is_dir={path.is_file()}\n"
        return output
    except Exception as e:
        return f"Error: {e}"


def get_file_content(working_directory, file_path) -> str:
    working_directory = Path(working_directory).resolve()
    file_path = working_directory.joinpath(file_path).resolve()

    if not file_path.is_relative_to(working_directory):
        return f'Error: Cannot read "{str(file_path)}" as it is outside the permitted working directory'
    if not file_path.is_file() or not file_path.exists():
        return f'Error: File not found or is not a regular file: "{str(file_path)}"'

    try:
        with file_path.open("r", encoding="utf-8") as f:
            content = f.read(config.MAX_CONTENT_LEN)

        if file_path.stat().st_size > config.MAX_CONTENT_LEN:
            return (
                content[: config.MAX_CONTENT_LEN]
                + f'[...File "{str(file_path)}" truncated at 10000 characters]'
            )
        return content

    except Exception as e:
        return f"Error: {e}"


def write_file(working_directory, file_path, content) -> str:
    working_directory = Path(working_directory).resolve()
    file_path = working_directory.joinpath(file_path).resolve()

    if not file_path.is_relative_to(working_directory):
        return f'Error: Cannot write to "{str(file_path)}" as it is outside the permitted working directory'

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open(mode="w", encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{str(file_path)}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
