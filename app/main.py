import os
from pathlib import Path


def move_file(command: str) -> None:
    split_command = command.split()
    _, source, destination = split_command
    source_filename = Path(source).name
    if "/" not in destination and "\\" not in destination:
        try:
            record_file = Path(source)
            record_file.rename(destination)
            return
        except FileExistsError:
            pass
    directories_to_create = []
    if destination[-1] == "/":
        split_path = destination.split("/")
        if split_path[0] == "":
            split_path.remove(split_path[0])
        split_path.pop()
        for directory in split_path:
            directories_to_create.append(directory)
        universal_path = os.path.join(*directories_to_create, source_filename)
        os.makedirs(os.path.dirname(universal_path), exist_ok=True)
        with (open(source, "r") as source_file,
              open(universal_path, "w") as record_file):
            text = source_file.read()
            record_file.write(text)
        os.remove(source)
        return
    if "/" in destination:
        split_path = destination.split("/")
    if "\\" in destination:
        split_path = destination.split("\\")
    destination_filename = split_path.pop()
    for directory in split_path:
        directories_to_create.append(directory)
    universal_path = os.path.join(*directories_to_create, destination_filename)
    os.makedirs(os.path.dirname(universal_path), exist_ok=True)
    with (open(source, "r") as source_file,
          open(universal_path, "w") as record_file):
        text = source_file.read()
        record_file.write(text)
    os.remove(source)
