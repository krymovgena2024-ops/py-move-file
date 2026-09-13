import os
from pathlib import Path


def move_file(command: str) -> None:
    split_command = command.split()
    if "/" not in split_command[2] or "\\" not in split_command[2]:
        try:
            record_file = Path(split_command[1])
            record_file.rename(split_command[2])
            return
        except FileNotFoundError:
            pass
    if "/" in split_command[2]:
        path = split_command[2]
        split_path = path.split("/")
    else:
        path = split_command[2]
        split_path = path.split("\\")
    directories_to_create = [split_path[0]]
    for directory in split_path[1:]:
        try:
            os.mkdir(os.path.join(*directories_to_create))
        except FileExistsError:
            pass
        directories_to_create.append(directory)
    universal_path = os.path.join(*directories_to_create)
    with (open(split_command[1], "r") as source_file,
          open(universal_path, "w") as record_file):
        text = source_file.read()
        record_file.write(text)
    os.remove(split_command[1])
