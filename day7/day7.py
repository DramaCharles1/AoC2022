import sys
from typing import Any, List, Dict
import re

def new_directory(directory_name, file_size, sub_directories: List[str]):
    directory = {"directory_name": directory_name,
                "file_size": file_size,
                "sub_directories": sub_directories}
    return directory

def main(input):
    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()
    #if line starts with $ its a command
    #if line starts with ls its listing current dir
    #if cd it changes dir to
    #for every cd keep track of in what directory you are in
    #for every ls that is made in a directory, save all directory content if it does not already exist

    all_directories = {}
    directories = []
    new_dir = False
    new_directory_name = ""
    new_dir_files = []
    new_dir_size = 0
    previous_line = "$ cd /"
    sub_directories = []
    for line in lines:
        if "$ ls" in line and "$ cd" in previous_line:
            new_dir = True
            new_directory_name = previous_line[4:]
            print(f"[DEBUG] New directory: {new_directory_name}")
        elif new_dir and not "$ cd" in line:
            print(f"[DEBUG] New file in directory {new_directory_name}: {line.strip()}")
            if len(re.findall(r'\d+', line)) > 0:
                #print(re.findall(r'\d+', line))
                new_dir_size += int(re.findall(r'\d+', line)[0])
            elif "dir" in line:
                sub_directories.append(line[4:])
        else:
            print(f"[DEBUG] Directory {new_directory_name} has a total size: {new_dir_size}")
            all_directories[new_directory_name] = new_directory(new_directory_name, new_dir_size, sub_directories)
            sub_directories = []
            new_dir = False
            new_dir_size = 0
        previous_line = line.strip()
    print(all_directories)

#search function that recursively searches through a directory and all sub directories and
#return total size

#def get_totalt_size_of_directory(directory_to_search: Dict[str:Any]):
#    files_in_directory = []
#    files_in_directory = directory_to_search["files"]
#    size = 0
#    for file in files_in_directory:
#        if "dir" in file:
#            pass
#        else:
#            size += int(re.findall(r'\d+', file)[0])

#def search_directory_helper(directory):
#    pass

if __name__ == "__main__":
    main(sys.argv[1])