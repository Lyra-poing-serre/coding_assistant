from pathlib import Path


def get_files_info(working_directory, directory=".") -> str:
    working_directory = Path(working_directory).resolve()
    directory = working_directory.joinpath(directory).resolve()

    if not directory.is_relative_to(working_directory):
        return f'Error: Cannot list "{str(object=directory)}" as it is outside the permitted working directory'
    if not directory.is_dir():
        return f'Error: "{str(directory)}" is not a directory'

    output = ""
    for path in directory.rglob("*"):
        output += f" - {path.name}: file_size={path.stat().st_size} bytes, is_dir={path.is_file()}\n"
    return output
