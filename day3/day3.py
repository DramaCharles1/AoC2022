import sys

def char_to_point(point_char: str):
    point = 0
    point = ord(point_char) #ascii value
    if point_char.islower():
        point = point - 96 #a is 1 point
    else:
        point = point - 38
    return point

def main(input):
    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()

    points = 0
    for line in lines:
        common_chars = []
        line_length = len(line[:-1])
        halves = [line[:int(line_length / 2)], line[int(line_length / 2):]]
        if not len(halves[0]) == len(halves[0]):
            raise Exception("halves are not correct")
        for temp_char_in_first_half in halves[0]:
            if temp_char_in_first_half in halves[1]:
                common_chars.append(temp_char_in_first_half)
        points = points + char_to_point(common_chars[0])
    print(f"point for part 1: {points}")

    groups_of_elves = []
    counter = 1
    temp_group = []
    for line in lines:
        if counter <= 2:
            temp_group.append(line)
            counter = counter + 1
        else:
            temp_group.append(line)
            groups_of_elves.append(temp_group)
            temp_group = []
            counter = 1

    points = 0
    common_chars = []
    common_chars_for_all_groups = []
    for group_of_elves in groups_of_elves:
        if len(group_of_elves) != 3:
            print(group_of_elves)
            raise Exception("wrong amount of elves!")
        for temp_char_in_first_line in group_of_elves[0]:
            if temp_char_in_first_line in group_of_elves[1]:
                common_chars.append(temp_char_in_first_line)
        for temp_char_in_third_line in group_of_elves[2]:
            if temp_char_in_third_line in common_chars:
                common_chars_for_all_groups.append(temp_char_in_third_line)
        points = points + char_to_point(common_chars_for_all_groups[0])
        common_chars_for_all_groups = []
        common_chars = []
    print(f"points for part 2: {points}")

if __name__ == "__main__":
    main(sys.argv[1])
