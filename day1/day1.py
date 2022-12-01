import sys

def main(input):
    lines = []
    with open(input) as file:
        lines = file.readlines()
    #print(f"[DEBUG] {lines}")

    elf_count = 0
    elf_calorie = 0
    elf_calorie_list = []
    for line in lines:
        if line == "\n":
            #print(f"[DEBUG] New elf with {elf_calorie} calories")
            elf_calorie_list.append(elf_calorie)
            elf_count = elf_count + 1
            elf_calorie = 0
        else:
            elf_calorie = elf_calorie + int(line.replace("\n",""))
    print(f"[DEBUG] elf count: {elf_count}")
    #print(f"[DEBUG] list {elf_calorie_list}")
    elf_calorie_list.sort(reverse=True)
    print(f"[DEBUG] list {elf_calorie_list}")
    #print(f"[DEBUG] sorted list {elf_calorie_list.sort()}")
    big_elf = 0
    #for elf in elf_calorie_list:
    #    if elf > big_elf:
    #        big_elf = elf
    #        print(f"yes new big elf: {big_elf}")
    #print(f"[DEBUG] biggest elf {big_elf}")
    #print(f"the elf with most calories: {elf_calorie_list.sort()}")


if __name__ == "__main__":
    main(sys.argv[1])