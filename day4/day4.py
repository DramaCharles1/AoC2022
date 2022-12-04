import sys

def sections_dics(smallest_id, biggest_id):
    sections = {"first_section": int(smallest_id),
                "last_section": int(biggest_id)}
    return sections

def main(input):
    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()

#if 2nd elf smallest section is bigger than 1st elf smallest section
# and 2nd elf biggest section is smaller than 1st elf biggest section
    sep = [',','-']
    same_sections = 0
    for line in lines:
        elf_pair = line.split(sep[0])
        _1st_elf_sections = sections_dics(elf_pair[0].split(sep[1])[0],
                                        elf_pair[0].split(sep[1])[1])
        _2nd_elf_sections = sections_dics(elf_pair[1].split(sep[1])[0],
                                        elf_pair[1].split(sep[1])[1])
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

    #find all pairs that dont overlap at all then minus the total amount of pairs
    same_sections = 0
    for line in lines:
        elf_pair = line.split(sep[0])
        _1st_elf_sections = sections_dics(elf_pair[0].split(sep[1])[0],
                                        elf_pair[0].split(sep[1])[1])
        _2nd_elf_sections = sections_dics(elf_pair[1].split(sep[1])[0],
                                        elf_pair[1].split(sep[1])[1])
        if _1st_elf_sections["last_section"] < _2nd_elf_sections["first_section"]:
            #print("---------------------")
            #print("first case")
            #print(f"[DEBUG] 1st elf sections: {_1st_elf_sections}")
            #print(f"[DEBUG] 2nd elf sections: {_2nd_elf_sections}")
            same_sections += 1
        if _2nd_elf_sections["last_section"] < _1st_elf_sections["first_section"]:
            #print("---------------------")
            #print("second case")
            #print(f"[DEBUG] 1st elf sections: {_1st_elf_sections}")
            #print(f"[DEBUG] 2nd elf sections: {_2nd_elf_sections}")
            same_sections += 1
    print(len(lines) - same_sections)

if __name__ == "__main__":
    main(sys.argv[1])
