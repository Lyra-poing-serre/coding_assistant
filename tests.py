from functions.run import run_python_file


if __name__ == "__main__":
    for file, content in [
        ("main.py", []),
        ("main.py", ["3 + 5"]),
        ("tests.py", []),
        ("../main.py", []),
        ("nonexistent.py", []),
    ]:
        print(run_python_file("calculator", file, content), end="\n\n")
