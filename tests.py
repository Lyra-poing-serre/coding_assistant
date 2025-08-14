from functions.files import get_file_content


if __name__ == "__main__":
    for file in ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]:
        print(get_file_content("calculator", file), end="\n\n")
