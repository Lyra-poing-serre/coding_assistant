from functions.files import get_files_info


if __name__ == "__main__":
    for directory in [".", "pkg", "/bin", "../"]:
        if directory == ".":
            print("Result for current directory:")
        else:
            print(f"Result for '{directory}' directory:")
        print(get_files_info("calculator", directory), end="\n\n")
