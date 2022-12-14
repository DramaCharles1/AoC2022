import sys

def main(input):
    print("Start")
    #Create map with size (smallest_x,0) to (biggest_x,biggest_y). Fill everything with air (.)
    #Fill in all rock formations on map by putting all rock coords into list. Fill in as (#)
    #Fill in sand coord on map (0,500). Fill in as (+)
    #Find rock formation with smallest coord (x) => set origo as 0,smallest_x
    #Find rock formation with biggest coord (y) => biggest_y
    #Find rock formation with biggest coord (x) => biggest_x
    #Find all rock coord and put into list
    #Find sand coord and put into list
    
    lines = []
    with open(input) as file:
        lines = file.readlines()
    
    smallest_x = 0
    biggest_x = 0
    biggest_y = 0
    
    start_smallest_x = int(lines[0].split(" ")[0].split(",")[0])
    print(start_smallest_x)
    line = "498,4 -> 498,6 -> 496,6"
    
    for line in lines:
        smallest_x, biggest_x, biggest_y = find_smallest_and_biggest_rock_coord_from_formation(line, start_smallest_x)
    #print(find_smallest_and_biggest_rock_coord_from_formation(line, start_smallest_x))
    print(f"[DEBUG] Map corners: {smallest_x, 0}, {biggest_x, 0}, {0, biggest_y}, {biggest_x, biggest_y}")
def find_smallest_and_biggest_rock_coord_from_formation(formation: str, old_smallest_x, old_biggest_x, old_biggest_y):
    sep = [" ", ","]
    smallest_x = old_smallest_x
    biggest_x = old_biggest_x
    biggest_y = old_biggest_y
    split_formation = formation.split(sep[0])
    for split in split_formation:
        if not split == "->":
            rock_coord = split.split(sep[1])
            if int(rock_coord[0]) < smallest_x:
                smallest_x = int(rock_coord[0])
            if int(rock_coord[0]) > biggest_x:
                biggest_x = int(rock_coord[0])
            if int(rock_coord[1]) > biggest_y:
                biggest_y = int(rock_coord[1])
    return smallest_x, biggest_x, biggest_y

if __name__ == "__main__":
    main(sys.argv[1])