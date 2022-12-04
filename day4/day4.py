import sys

def sections_dics(smallest_id, biggest_id):
    sections = {"first_section": int(smallest_id),
                "last_section": int(biggest_id)}
    return sections

def main(input):
    #get line, divide into 2 elves
    #check if 1st elf biggest sectio ID is bigger or equal to 2nd elf's smallest number
    #and if 1st elf biggest section ID is smaller or equal to 2nd elf's biggest number
    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()
    
    line = lines[0]
    sep = [',','-']
    elf_pair = line.split(sep[0])

    print(elf_pair[0].split(sep[1])[0])
    print(elf_pair[0].split(sep[1])[1])
    print(elf_pair[1].split(sep[1])[0])
    print(elf_pair[1].split(sep[1])[1])


    _1st_elf_sections = sections_dics(elf_pair[0].split(sep[1])[0], elf_pair[0].split(sep[1])[1])
    _2nd_elf_sections = sections_dics(elf_pair[1].split(sep[1])[0], elf_pair[1].split(sep[1])[1])

    print(elf_pair)
    print(_1st_elf_sections)

    same_sections = 0
    if _1st_elf_sections["last_section"] >= _2nd_elf_sections["first_section"]:
        same_sections = same_sections + 1
    print(same_sections)

#if 2nd elf smallest section is bigger than 1st elf smallest section and 2nd elf biggest section is smaller than 1st elf biggest section
    same_sections = 0
    for line in lines:
        elf_pair = line.split(sep[0])
        _1st_elf_sections = sections_dics(elf_pair[0].split(sep[1])[0], elf_pair[0].split(sep[1])[1])
        _2nd_elf_sections = sections_dics(elf_pair[1].split(sep[1])[0], elf_pair[1].split(sep[1])[1])
        if _2nd_elf_sections["first_section"] == _1st_elf_sections["first_section"] and _2nd_elf_sections["last_section"] == _1st_elf_sections["last_section"]:
            print(f"[DEBUG] the same sections")
            print(f"[DEBUG] 1st elf sections: {_1st_elf_sections}")
            print(f"[DEBUG] 2nd elf sections: {_2nd_elf_sections}")
        if _2nd_elf_sections["first_section"] >= _1st_elf_sections["first_section"] and _2nd_elf_sections["last_section"] <= _1st_elf_sections["last_section"]:
            #print("---------------------")
            #print(f"[DEBUG] 2nd elf's sections included in 1st elf's")
            #print(f"[DEBUG] 1st elf sections: {_1st_elf_sections}")
            #print(f"[DEBUG] 2nd elf sections: {_2nd_elf_sections}")
            same_sections = same_sections + 1
        elif _1st_elf_sections["first_section"] >= _2nd_elf_sections["first_section"] and _1st_elf_sections["last_section"] <= _2nd_elf_sections["last_section"]:
            #print("---------------------")
            #print(f"[DEBUG] 1st elf's sections included in 2nd elf's")
            #print(f"[DEBUG] 1st elf sections: {_1st_elf_sections}")
            #print(f"[DEBUG] 2nd elf sections: {_2nd_elf_sections}")
            same_sections = same_sections + 1

    print(same_sections)

if __name__ == "__main__":
    main(sys.argv[1])