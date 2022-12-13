import sys

def main(input):
    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()

    rows = []
    cols = []

    for line in lines:
        line = line.strip()
        rows.append(line)

    for row in rows:
        for x in range(0, len(row)):
            try:
                cols[x] += row[x]
            except IndexError:
                cols.append("")
                cols[x] += row[x]

    x = 0
    y = 0
    current_tree_height = 0
    left = []
    right = []
    up = []
    down = []
    visable_trees = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0]) - 1):
            current_tree_height = lines[y][x]
            #print(f"current tree coord: {x},{y}")
            if x == 0 or y == 0 or x == len(lines[0]) - 2 or y == len(lines) - 1: #check if on a vertical edge
                #print(f"[DEBUG] current tree is on an edge: {current_tree_height}")
                visable_trees += 1
            else:
                #print(f"[DEBUG] current tree height: {current_tree_height}")
                left = rows[y][:x]
                right = rows[y][x+1:]
                up = cols[x][:y]
                down = cols[x][y+1:]
                #print(f"[DEBUG] left: {left}")
                #print(f"[DEBUG] right: {right}")
                #print(f"[DEBUG] up: {up}")
                #print(f"[DEBUG] down: {down}")
                if check_if_tree_is_higher(current_tree_height, left, right, down, up):
                    visable_trees += 1
        #print("------------")
    print(f"[DEBUG] Part 1 visable trees: {visable_trees}")

    best_scenic_score = 0
    current_coord = [0,0]
    best_coord = [0,0]
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0]) - 1):
            current_coord[0] = x
            current_coord[1] = y
            #print(f"current tree coord: {current_coord[0]},{current_coord[1]}")
            current_tree_height = int(lines[y][x])
            #print(f"current tree height: {current_tree_height}")
            left = rows[y][:x]
            right = rows[y][x+1:]
            up = cols[x][:y]
            down = cols[x][y+1:]
            edge = False
            if x == 0 or y == 0 or x == len(lines[0]) - 2 or y == len(lines) - 1:
                edge = True
            current_scenic_score = scenic_score(current_tree_height, edge, left, right, up, down)
            #print(f"[DEBUG] current scenic score: {current_scenic_score}")
            if current_scenic_score  > best_scenic_score:
                best_scenic_score = current_scenic_score
                best_coord[0] = current_coord[0]
                best_coord[1] = current_coord[1]
            #print("-------------")
    print(f"[DEBUG] Part 2 best scenic score : {best_scenic_score} at coord {best_coord}")

def scenic_score(current_tree, edge: bool, left: str, right: list, up: list, down: list):
    if edge:
        #print(f"[DEBUG] edge")
        return 0
    left_score = 0
    right_score = 0
    up_score = 0
    down_score = 0

    left = left[::-1]
    for x in left:
        if current_tree > int(x):
            #print(f"[DEBUG] next left that can be seen: {int(x)}")
            left_score += 1
        else:
            #print(f"[DEBUG] next left that can be seen: {int(x)}")
            left_score += 1
            break

    for x in right:
        if current_tree > int(x):
            #print(f"[DEBUG] next right that can be seen: {int(x)}")
            right_score += 1
        else:
            #print(f"[DEBUG] next right that can be seen: {int(x)}")
            right_score += 1
            break

    up = up[::-1]
    for x in up:
        if current_tree > int(x):
            #print(f"[DEBUG] next up that can be seen: {int(x)}")
            up_score += 1
        else:
            #print(f"[DEBUG] next up that can be seen: {int(x)}")
            up_score += 1
            break

    for x in down:
        if current_tree > int(x):
            #print(f"[DEBUG] next down that can be seen: {int(x)}")
            down_score += 1
        else:
            #print(f"[DEBUG] next down that can be seen: {int(x)}")
            down_score += 1
            break
    #print(f"[DEBUG] {left_score} {right_score} {up_score} {down_score}")
    return left_score * right_score * up_score * down_score

def check_if_tree_is_higher(current_tree, left, right, up, down):
    return current_tree > max(left) or current_tree > max(right) or current_tree > max(up) or current_tree > max(down)

if __name__ == "__main__":
    main(sys.argv[1])
