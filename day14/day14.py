import sys
import time

def main(input):
    print("Start")
    start = time.time()
    lines = []
    with open(input) as file:
        lines = file.readlines()

    global sep
    sep = [" ", "," ," -> "]

    rock_coords = []
    for line in lines:
        for rock in rock_formation_to_coords(line):
            rock = rock.strip()
            if not rock in rock_coords:
                rock_coords.append(rock)

    old_smallest_x = int(rock_coords[0].split(",")[0])
    old_biggest_x = old_smallest_x
    old_biggest_y = int(rock_coords[0].split(",")[1])

    smallest_x = old_smallest_x
    biggest_x = old_biggest_x
    biggest_y = old_biggest_y
    for rock in rock_coords:
        smallest_x, biggest_x, biggest_y = find_smallest_and_biggest_rock_coord_from_all_rocks(rock, smallest_x, biggest_x, biggest_y)
    print(f"[DEBUG] Map corners: {smallest_x, 0}, {biggest_x, 0}, {0, biggest_y}, {biggest_x, biggest_y}")

    sand_coords = []
    rock_and_sand_coords = []
    rock_and_sand_coords.extend(rock_coords)
    start_coord = "500,0"
    for i in range(0,832):
        #print(i) #show progress
        add_sand = fill_sand(start_coord, rock_and_sand_coords)
        #print(f"sand to add: {add_sand}")
        #print(f"sand coords: {sand_coords}")
        if add_sand is None:
            break
        sand_coords.append(add_sand)
        rock_and_sand_coords.append(add_sand)

    ##Show map
    #map = []
    #for y in range(0, biggest_y + 1):
    #    map_line = []
    #    for x in range(smallest_x, biggest_x + 1):
    #        coord = f"{x},{y}"
    #        if coord in rock_coords:
    #            map_line.append("#")
    #        elif coord in "500,0":
    #            map_line.append("+")
    #        elif coord in sand_coords:
    #            map_line.append("O")
    #        else:
    #            map_line.append(".")
    #    print(map_line)
    #    map.append(map_line)
    sand_coords.append(start_coord)
    print(f"Result part 1: {len(sand_coords)}")

    print("Start part 2")
    etc = 400
    smallest_x = smallest_x - etc
    biggest_x = biggest_x + etc
    biggest_y = biggest_y + 2
    print(f"[DEBUG] Map corners: {smallest_x, 0}, {biggest_x, 0}, {0, biggest_y}, {biggest_x, biggest_y}")
    floor = []
    for i in range(smallest_x, biggest_x + 1):
        floor_coord = f"{i},{biggest_y}"
        floor.append(floor_coord)
    rock_coords.extend(floor)

    sand_coords = []
    rock_and_sand_coords = []
    rock_and_sand_coords.extend(rock_coords)
    for i in range(0,100000):
        #print(i)
        add_sand = fill_sand2(start_coord, rock_and_sand_coords, biggest_y)
        #print(f"sand to add: {add_sand}")
        #print(f"sand coords: {sand_coords}")
        if add_sand is None or add_sand == start_coord:
            break
        sand_coords.append(add_sand)
        #rock_and_sand_coords.append(add_sand) #1209.1734318733215s
        rock_and_sand_coords.insert(0,add_sand) #760.30299949646s

    ##Show map
    #map = []
    #for y in range(0, biggest_y + 1):
    #    map_line = []
    #    for x in range(smallest_x, biggest_x + 1):
    #        coord = f"{x},{y}"
    #        if coord in rock_coords:
    #            map_line.append("#")
    #        elif coord in start_coord:
    #            map_line.append("+")
    #        elif coord in sand_coords:
    #            map_line.append("O")
    #        else:
    #            map_line.append(".")
        #print(map_line)
        #map.append(map_line)
    sand_coords.append(start_coord)
    print(f"Result part 2: {len(sand_coords)}")
    print(f"elapsed time: {time.time() - start}s")

def fill_sand(start_coord: str, rock_and_sand_coords: list):
    coord_to_check = start_coord
    while True:
        if f"{int(coord_to_check.split(sep[1])[0])},{int(coord_to_check.split(sep[1])[1]) + 1}" not in rock_and_sand_coords:
            coord_to_check = f"{int(coord_to_check.split(sep[1])[0])},{int(coord_to_check.split(sep[1])[1]) + 1}"
        elif f"{int(coord_to_check.split(sep[1])[0]) - 1},{int(coord_to_check.split(sep[1])[1]) + 1}" not in rock_and_sand_coords:
            coord_to_check = f"{int(coord_to_check.split(sep[1])[0]) - 1},{int(coord_to_check.split(sep[1])[1]) + 1}"
        elif f"{int(coord_to_check.split(sep[1])[0]) + 1},{int(coord_to_check.split(sep[1])[1]) + 1}" not in rock_and_sand_coords:
            coord_to_check = f"{int(coord_to_check.split(sep[1])[0]) + 1},{int(coord_to_check.split(sep[1])[1]) + 1}"
        else:
            return coord_to_check

def fill_sand2(start_coord: str, rock_and_sand_coords: list, floor_height: int):
    coord_to_check = start_coord
    count = 0
    stop_flag = False
    while True:
        if int(coord_to_check.split(sep[1])[1]) == floor_height:
            return coord_to_check
        elif f"{int(coord_to_check.split(sep[1])[0])},{int(coord_to_check.split(sep[1])[1]) + 1}" not in rock_and_sand_coords:
            coord_to_check = f"{int(coord_to_check.split(sep[1])[0])},{int(coord_to_check.split(sep[1])[1]) + 1}"
            count += 1
        elif f"{int(coord_to_check.split(sep[1])[0]) - 1},{int(coord_to_check.split(sep[1])[1]) + 1}" not in rock_and_sand_coords or stop_flag:
            coord_to_check = f"{int(coord_to_check.split(sep[1])[0]) - 1},{int(coord_to_check.split(sep[1])[1]) + 1}"
        elif f"{int(coord_to_check.split(sep[1])[0]) + 1},{int(coord_to_check.split(sep[1])[1]) + 1}" not in rock_and_sand_coords or stop_flag:
            coord_to_check = f"{int(coord_to_check.split(sep[1])[0]) + 1},{int(coord_to_check.split(sep[1])[1]) + 1}"
        else:
            return coord_to_check

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
    #print(f"rocks to add: {rocks_to_add}")
    return rocks_to_add

if __name__ == "__main__":
    main(sys.argv[1])
