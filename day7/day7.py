import sys
from typing import Any, List, Dict
import re
import random
import string
import pdb

def new_directory(directory_name, parrent_directory, file_size, sub_directories: List[str], files: List[str]):
    directory = {"directory_name": directory_name,
                "parrent_directory": parrent_directory,
                "file_size": file_size,
                "sub_directories": sub_directories,
                "total_size": 0,
                "files": files}
    return directory

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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
    all_directories2 = {}
    all_directories3 = []
    previous_line = ""
    current_directory = ""
    parrent_directory = ""
    current_directory_size = 0
    subdirectories = []
    files = []
    list_directory = False
    directory_id = ""
    current_path = ""
    for line in lines:
        line = line.strip()
        #print(f"line: {line}")
        if "$ cd .." in line:
            if list_directory:
                print(f"Add new directory: {current_path}")
                print(f"New directory {current_path} directory name {current_directory}")
                print(f"New directory {current_path} parrent directory {parrent_directory}")
                print(f"New directory {current_path} total size: {current_directory_size}")
                print(f"New directory {current_path} subdirectories: {subdirectories}")
                print(f"New directory {current_path} files: {files}")
                all_directories2[current_path] = new_directory(current_path, parrent_directory, current_directory_size, subdirectories, files)
                all_directories3.append(new_directory(current_path, parrent_directory, current_directory_size, subdirectories, files))
                subdirectories = []
                files = []
                current_directory_size = 0
            if current_path == "/":
                pass
            else:
                current_path_list = current_path.split("/")
                current_path_list = current_path_list[0:len(current_path_list) - 2]
                print(current_path_list)
                current_path = ""
                for path in current_path_list:
                    print(f"path build: {path}")
                    #current_directory += f"/{path}"
                    current_path += f"{path}/"
            print(f"Current path: {current_path}")
            list_directory = False
        elif "$ cd" in line:
            if list_directory:
                print(f"Add new directory: {current_path}")
                print(f"New directory {current_path} directory name {current_directory}")
                print(f"New directory {current_path} parrent directory {parrent_directory}")
                print(f"New directory {current_path} total size: {current_directory_size}")
                print(f"New directory {current_path} subdirectories: {subdirectories}")
                print(f"New directory {current_path} files: {files}")
                all_directories2[current_path] = new_directory(current_path, parrent_directory, current_directory_size, subdirectories, files)
                all_directories3.append(new_directory(current_path, parrent_directory, current_directory_size, subdirectories, files))
                subdirectories = []
                files = []
                current_directory_size = 0
            if "$ cd /" in line:
                current_path = "/"
            else:
                #curren_directory = e
                #/asd
                current_directory = line.split(" ")[-1]
                #current_directory = current_path.split("/")[-1]
                current_path += f"{current_directory}/"
            parrent_directory = current_directory
            print(f"current directory: {current_directory}")
            print(f"current path: {current_path}")
            list_directory = False
        elif "$ ls" in line:
            list_directory = True
        elif "end" in line:
            if list_directory:
                print(f"Add new directory: {current_path}")
                print(f"New directory {current_path} directory name {current_directory}")
                print(f"New directory {current_path} parrent directory {parrent_directory}")
                print(f"New directory {current_path} total size: {current_directory_size}")
                print(f"New directory {current_path} subdirectories: {subdirectories}")
                print(f"New directory {current_path} files: {files}")
                all_directories2[current_path] = new_directory(current_path, parrent_directory, current_directory_size, subdirectories, files)
                all_directories3.append(new_directory(current_path, parrent_directory, current_directory_size, subdirectories, files))
                subdirectories = []
                files = []
                current_directory_size = 0
            list_directory = False
        elif list_directory:
            if len(re.findall(r'\d+', line)) > 0:
                file = line.split(" ")
                current_directory_size += int(file[0]) #if size is in beginning of string
                files.append(file[1])
            elif "dir":
                subdirectory = line.split(" ")[1]
                subdirectory = f"{current_path}{subdirectory}/"
                subdirectories.append(subdirectory)
        previous_line = line
    print("--------------------------------------------------")
    print(f"Amount of directories: {len(all_directories2)}")
    print("--------------------------------------------------")
    for directory in all_directories2.keys():
        print(f"Directory: {all_directories2[directory]['directory_name']}")
        print(f"Parrent directory:: {all_directories2[directory]['parrent_directory']}")
        print(f"Directory size:: {all_directories2[directory]['file_size']}")
        print(f"Directory subdirectories:: {all_directories2[directory]['sub_directories']}")
        print(f"Directory files:: {all_directories2[directory]['files']}")
        print("--------------------")
    print("--------------------------------------------------")
    size_less_than_100k = 0
    for directory in all_directories2.keys():
        size = search_helper2(directory, all_directories2)
        if size <= 100000:
            size_less_than_100k += size
        all_directories2[directory]["total_size"] = size
        print(f"Directory {all_directories2[directory]['directory_name']} total size: {all_directories2[directory]['file_size']}")
    print("--------------------------------------------------")
    print(f"Result part 1: {size_less_than_100k}")
    size_used = all_directories2["/"]["total_size"] 
    total_size = 70000000
    print(f"Total size: {total_size}")
    print(f"Size used: {size_used}")
    print(f"Size needed for update: {30000000}")
    size_needed = size_used - 30000000
    print(f"Size needed: {size_needed}")
    delta = 0
    old_delta = 70000000
    found_directory = {}
    print("--------------------------------------------------")
    for dir in all_directories2:
        print(dir)
        print(all_directories2[dir]["total_size"])
        if all_directories2[dir]["total_size"] >= size_needed:
            print("yes")
    print("--------------------------------------------------")
    for directory in all_directories2:
        #print(f"directory {directory} total size: {all_directories2[directory]['total_size']}")
        if all_directories2[directory]["total_size"] >= size_needed:
            print(f"potential dir to delete found: {found_directory} with total size {all_directories2[directory]['total_size']}")
            delta = all_directories2[directory]["total_size"] - size_needed
            if delta < 0:
                raise Exception("something went wrong")
            if delta < old_delta:
                found_directory = directory
                old_delta = delta
                print(f"new dir to delete found: {found_directory} with total size {all_directories2[directory]['total_size']}")
    print(old_delta)
    for key in all_directories2[found_directory].keys():
        print(f"{key}: {all_directories2[found_directory][key]}")

def search_helper2(search_directory, all_directories: Dict):
    temp_directory = all_directories[search_directory]
    sub_directories = temp_directory["sub_directories"]
    #print(f"i will now search through dir {search_directory} with its subdirecories {sub_directories}")
    size = temp_directory["file_size"]
    if len(sub_directories) > 0:
        for i in range(0, len(sub_directories)):
            size += search_helper2(sub_directories[i], all_directories)
    return size

def search_helper(search_directory):
    temp_directory = all_directories[search_directory]
    sub_directories = temp_directory["sub_directories"]
    #print(f"i will now search through dir {search_directory} with its subdirecories {sub_directories}")
    size = temp_directory["file_size"]
    if len(sub_directories) > 0:
        for i in range(0, len(sub_directories)):
            size += search_helper(sub_directories[i])
    return size

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