import sys

def main(input):
    lines = []
    with open(input) as file:
        lines = file.readlines()

    elf_count = 0
    elf_calorie = 0
    elf_calorie_list = []
    for line in lines:
        if line == "\n":
            elf_calorie_list.append(elf_calorie)
            elf_count = elf_count + 1
            elf_calorie = 0
        else:
            elf_calorie = elf_calorie + int(line.replace("\n",""))
    print(f"[DEBUG] elf count: {elf_count}")
    elf_calorie_list.sort(reverse=True)
    print(f"[DEBUG] list {elf_calorie_list}")
    big_elf = elf_calorie_list[0]
    print(f"[DEBUG] biggest elf {big_elf}")
    top_three_biggest_elves = elf_calorie_list[0] + elf_calorie_list[1] + elf_calorie_list[2]
    print(f"[DEBUG] top 3 biggest elves {top_three_biggest_elves}")


if __name__ == "__main__":
    main(sys.argv[1])