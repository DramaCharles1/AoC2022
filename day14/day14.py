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
    
    global sep
    sep = [" ", "," ," -> "]

    line = "498,4 -> 498,6 -> 496,6"
    #rint(rock_formation_to_coords(line))
    
    rock_coords = []
    for line in lines:
        #smallest_x, biggest_x, biggest_y = find_smallest_and_biggest_rock_coord_from_formation(line, start_smallest_x)
        #print(rock_formation_to_coords(line))
        for rock in rock_formation_to_coords(line):
            rock = rock.strip()
            if not rock in rock_coords:
                rock_coords.append(rock)
    print(rock_coords)
    print(len(rock_coords))
    old_smallest_x = int(rock_coords[0].split(",")[0])
    old_biggest_x = old_smallest_x
    old_biggest_y = int(rock_coords[0].split(",")[1])
    #print(old_smallest_x, old_biggest_x, old_biggest_y)

    smallest_x = old_smallest_x
    biggest_x = old_biggest_x
    biggest_y = old_biggest_y
    for rock in rock_coords:
        smallest_x, biggest_x, biggest_y = find_smallest_and_biggest_rock_coord_from_all_rocks(rock, smallest_x, biggest_x, biggest_y)
    print(f"[DEBUG] Map corners: {smallest_x, 0}, {biggest_x, 0}, {0, biggest_y}, {biggest_x, biggest_y}")
    sand_fill = 0


def find_smallest_and_biggest_rock_coord_from_all_rocks(rock: str, old_smallest_x, old_biggest_x, old_biggest_y):
    x = int(rock.split(sep[1])[0])
    y = int(rock.split(sep[1])[1])
    smallest_x = 0
    biggest_x = 0
    biggest_y = 0
    if x < old_smallest_x:
        smallest_x = x
    else:
        smallest_x = old_smallest_x
    if x > old_biggest_x:
        biggest_x = x
    else:
        biggest_x = old_biggest_x
    if y > old_biggest_y:
        biggest_y = y
    else:
        biggest_y = old_biggest_y
    return smallest_x, biggest_x, biggest_y

def rock_formation_to_coords(formation: str):
    rocks = formation.split(sep[2])
    print(f"rocks: {rocks}")
    rocks_to_add = []
    for i in range(0,len(rocks)):
        current_rock = rocks[i]
        try:
            next_rock = rocks[i + 1]
        except IndexError:
            rocks_to_add.append(current_rock)
            break
        #check direction to fill in rocks to rock_coord
        current_rock_x = int(current_rock.split(sep[1])[0])
        next_rock_x = int(next_rock.split(sep[1])[0])
        current_rock_y = int(current_rock.split(sep[1])[1])
        next_rock_y = int(next_rock.split(sep[1])[1])
        #print(f"current rock: {current_rock_x},{current_rock_y}")
        #print(f"next rock: {next_rock_x},{next_rock_y}")
        diff_x = next_rock_x - current_rock_x
        diff_y = next_rock_y - current_rock_y
        if diff_x != 0:
            for j in range(0,abs(diff_x)):
                if diff_x > 0:
                    temp_rock = f"{current_rock_x+j},{current_rock_y}"
                    #print(f"rock to add in positive x direction: {temp_rock}")
                    rocks_to_add.append(temp_rock)
                else:
                    temp_rock = f"{current_rock_x-j},{current_rock_y}"
                    #print(f"rock to add in negative x direction: {temp_rock}")
                    rocks_to_add.append(temp_rock)
        else:
            for j in range(0,abs(diff_y)):
                if diff_y > 0:
                    temp_rock = f"{current_rock_x},{current_rock_y+j}"
                    #print(f"rock to add in positive y direction: {temp_rock}")
                    rocks_to_add.append(temp_rock)
                else:
                    temp_rock = f"{current_rock_x},{current_rock_y-j}"
                    #print(f"rock to add in negative y direction: {temp_rock}")
                    rocks_to_add.append(temp_rock)
    print(f"rocks to add: {rocks_to_add}")
    return rocks_to_add

if __name__ == "__main__":
    main(sys.argv[1])