import sys
from typing import Any, List, Dict
import re
import random
import string

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
    for line in lines:
        line = line.strip()
        #print(f"line: {line}")
        if "$ cd .." in line:
            if list_directory:
                directory_id = id_generator()
                print(f"Add new directory: {directory_id}")
                print(f"New directory {directory_id} directory name {current_directory}")
                print(f"New directory {directory_id} parrent directory {parrent_directory}")
                print(f"New directory {directory_id} total size: {current_directory_size}")
                print(f"New directory {directory_id} subdirectories: {subdirectories}")
                print(f"New directory {directory_id} files: {files}")
                all_directories2[directory_id] = new_directory(current_directory, parrent_directory, current_directory_size, subdirectories, files)
                all_directories3.append(new_directory(current_directory, parrent_directory, current_directory_size, subdirectories, files))
                subdirectories = []
                files = []
                current_directory_size = 0
            current_directory = ""
            list_directory = False
        elif "$ cd" in line:
            if list_directory:
                directory_id = id_generator()
                print(f"Add new directory: {directory_id}")
                print(f"New directory {directory_id} directory name {current_directory}")
                print(f"New directory {directory_id} parrent directory {parrent_directory}")
                print(f"New directory {directory_id} total size: {current_directory_size}")
                print(f"New directory {directory_id} subdirectories: {subdirectories}")
                print(f"New directory {directory_id} files: {files}")
                all_directories2[directory_id] = new_directory(current_directory, parrent_directory, current_directory_size, subdirectories, files)
                all_directories3.append(new_directory(current_directory, parrent_directory, current_directory_size, subdirectories, files))
                subdirectories = []
                files = []
                current_directory_size = 0
            parrent_directory = current_directory
            current_directory = line.split(" ")[2]
            print(f"current directory: {current_directory}")
            list_directory = False
        elif "$ ls" in line:
            list_directory = True
        elif "end" in line:
            if list_directory:
                directory_id = id_generator()
                print(f"Add new directory: {directory_id}")
                print(f"New directory {directory_id} directory name {current_directory}")
                print(f"New directory {directory_id} parrent directory {parrent_directory}")
                print(f"New directory {directory_id} total size: {current_directory_size}")
                print(f"New directory {directory_id} subdirectories: {subdirectories}")
                print(f"New directory {directory_id} files: {files}")
                all_directories2[directory_id] = new_directory(current_directory, parrent_directory, current_directory_size, subdirectories, files)
                all_directories3.append(new_directory(current_directory, parrent_directory, current_directory_size, subdirectories, files))
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
        all_directories2[directory]["total_size"] = size
        print(f"Directory {all_directories2[directory]['directory_name']} total size: {all_directories2[directory]['file_size']}")
    print("--------------------------------------------------")
    #print(f"Amount of directories: {len(all_directories2)}")
    #print("--------------------------------------------------")
    #for directory in all_directories2.keys():
    #    print(f"Directory: {all_directories2[directory]['directory_name']}")
    #    print(f"Parrent directory: {all_directories2[directory]['parrent_directory']}")
    #    print(f"Directory size: {all_directories2[directory]['file_size']}")
    #    print(f"Directory subdirectories: {all_directories2[directory]['sub_directories']}")
    #    print(f"Directory files: {all_directories2[directory]['files']}")
    #    print("--------------------")
    #print("--------------------------------------------------")
    #size_less_than_100k = 0
    #for directory in all_directories2:
    #    size = search_helper2(directory, all_directories2)
    #    all_directories2[directory]["total_size"] = size
    #    print(f"Directory {all_directories2[directory]['directory_name']} total size: {all_directories2[directory]['file_size']}")
    #print("--------------------------------------------------")

    #global all_directories
    #all_directories = {}
    #directories = []
    #new_dir = False
    #new_directory_name = ""
    #new_dir_files = []
    #new_dir_size = 0
    #previous_line = "$ cd /"
    #sub_directories = []
    #for line in lines:
    #    line = line.strip()
    #    if "end" in line:
    #        new_dir = False
    #    elif "$ ls" in line and "$ cd" in previous_line:
    #        new_dir = True
    #        new_directory_name = previous_line[5:]
    #        #print(f"[DEBUG] New directory: {new_directory_name}")
    #    elif new_dir and not "$ cd" in line:
    #        #print(f"[DEBUG] New file in directory {new_directory_name}: {line.strip()}")
    #        if len(re.findall(r'\d+', line)) > 0:
    #            #print(re.findall(r'\d+', line))
    #            new_dir_size += int(re.findall(r'\d+', line)[0])
    #        elif "dir" in line:
    #            sub_directories.append(line[4:len(line) - 1])
    #        else:
    #            raise Exception("something went wrong")
    #    elif "cd .." in line:
    #        pass
    #    else:
    #        #print(f"[DEBUG] Directory {new_directory_name} has a total size: {new_dir_size}")
    #        if new_directory_name not in all_directories.keys():
    #            all_directories[new_directory_name] = new_directory(new_directory_name, new_dir_size, sub_directories)
    #        sub_directories = []
    #        new_dir = False
    #        new_dir_size = 0
    #    previous_line = line
    ##print(f"Amount of directories: {len(all_directories)}")
    ##debug = "tjtccqtm"
    ##print(f"[DEBUG] directory {debug} has a total size of: {search_helper(debug)}")
    ##debug = "/"
    ##print(f"[DEBUG] directory {debug} has a total size of: {search_helper(debug)}")
    #size_less_than_100k = 0
    #for directory in all_directories:
    #    if directory != "":
    #        size = search_helper(directory)
    #        all_directories[directory]["total_size"] = size
    #        if size <= 100000:
    #            #print(f"[DEBUG] directory {directory} has a total size of: {size}")
    #            #print(f"[DEBUG] directory {directory} has a total size less than 100000")
    #            size_less_than_100k += size
    #print(f"result: {size_less_than_100k}")

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