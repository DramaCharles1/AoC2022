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
    #split line in 2
    line = lines[2]
    print(f"[DEBUG] line: {line}")
    print(f"[DEBUG] line length: {len(line[:-1])}")
    line_length = len(line[:-1])
    print(f"[DEBUG] 1st half: {line[:int(line_length / 2)]}")
    print(f"[DEBUG] 2nd half: {line[int(line_length / 2):]}")
    halves = [line[:int(line_length / 2)], line[int(line_length / 2):]]
    print(halves)
    #find common char in both halves
    common_chars = []
    for temp_char_in_first_half in halves[0]:
        if temp_char_in_first_half in halves[1]:
            common_chars.append(temp_char_in_first_half)
    print(f"[DEBUG] common chars: {common_chars}")
    #get prio points for common char
    print(ord('a'))
    for x in common_chars:
        print(f"point from prio: {char_to_point(x)}")
    print(f"point from prio: {char_to_point('z')}")
    print(f"point from prio: {char_to_point('Z')}")

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
        print(common_chars)

    print(f"point from all: {points}")
    #add prio points to total score

    #part 2
    #group lines into 3
    #find common char in each group
    #get prio point for that char
    group = [lines[0],lines[1],lines[2]]
    print(group)
    common_chars = []
    for temp_char_in_first_line in group[0]:
        if temp_char_in_first_line in group[1]:
            common_chars.append(temp_char_in_first_line)
    for temp_char_in_third_line in group[2]:
        if temp_char_in_third_line in common_chars:
            print(f"found common char: {temp_char_in_third_line}")
    print(common_chars)

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
    common_chars_again = []
    for group_of_elves in groups_of_elves:
        if len(group_of_elves) is not 3:
            print(group_of_elves)
            raise Exception("wrong amount of elves!")
        for temp_char_in_first_line in group_of_elves[0]:
            if temp_char_in_first_line in group_of_elves[1]:
                common_chars.append(temp_char_in_first_line)
        for temp_char_in_third_line in group_of_elves[2]:
            if temp_char_in_third_line in common_chars:
                print(f"found common char: {temp_char_in_third_line}")
                common_chars_again.append(temp_char_in_third_line)
        points = points + char_to_point(common_chars_again[0])
        common_chars_again = []
        common_chars = []
    print(points)

if __name__ == "__main__":
    main(sys.argv[1])