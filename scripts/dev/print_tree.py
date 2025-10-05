import os


import os

def print_tree(root, ignore_dir: list[str] = None, ignore_ext: list[str] = None, prefix="", level=2):
    """
    Prints a directory tree structure, ignoring specified directories, files, and extensions.

    Args:
        root (str): The starting directory path.
        ignore_dir (list[str]): List of directory or file names to ignore.
        ignore_ext (list[str]): List of file extensions to ignore (e.g., ['.pyc', '.log']).
        prefix (str): Visual prefix for tree indentation.
        level (int): Depth level to print (0 = only current directory).
    """
    if level < 0:
        return

    ignore_dir = ignore_dir or []
    ignore_ext = ignore_ext or []

    try:
        files = sorted(os.listdir(root))
    except PermissionError:
        print(prefix + "├── [Permission Denied]")
        return

    for f in files:
        if f in ignore_dir:
            continue
        
        path = os.path.join(root, f)

        # Skip if file has ignored extension
        if os.path.isfile(path):
            _, ext = os.path.splitext(f)
            if ext in ignore_ext:
                continue

        print(prefix + "├── " + f)

        if os.path.isdir(path):
            print_tree(path, ignore_dir, ignore_ext, prefix + "│   ", level - 1)

if __name__ == "__main__":
    print_tree(
        root=".",
        ignore_dir=['.git', "__pycache__"],
        ignore_ext=[],
        prefix="",
        level=1)