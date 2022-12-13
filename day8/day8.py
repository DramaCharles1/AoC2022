import sys

def main(input):
    #edges
    #count trees in first line
    #count 2 trees per line
    #count trees last line
    
    #get current_tree height
    #get current_tree neighbor left[], right[], up[], down[]
    #for tree in range(0,len(left) + 1): 
    #    if tree == len(left) + 1):
    #       #if we come here we increase visable_tree
    #    if current_tree_height > tree:
    #       pass
    #    else:
    #       break #then we now another tree is higher than current_tree

    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()
    
    rows = []
    cols = []
    
    #123
    #345
    #678
    
    for line in lines:
        line = line.strip()
        rows.append(line)
    
    cols2 = [""] * len(rows[0])
    test = ""
    test += "1"
    
    print("------------")
    for row in rows:
        print(row)
        for x in range(0, len(row)):
            try:
                cols[x] += row[x]
                #cols[x].append(row[x])
            except IndexError as list_error:
                cols.append("")
                cols[x] += row[x]
                #cols[x].append(row[x])
                
    #print(cols2)
                

    horizontal_edges = len(lines[0]) - 1
    vertical_edges = len(lines)

    #print(horizontal_edges)
    #print(vertical_edges)
    edges = horizontal_edges * 2 + vertical_edges * 2 - 4
    #print(edges)
    x = 0
    y = 0
    current_tree_height = 0
    left = []
    right = []
    up = []
    down = []
    visable_trees = 0
    #print(f"line len {len(lines[0])}")
    #print("------------")
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0]) - 1):
            current_tree_height = lines[y][x]
            #print(f"current tree coord: {x},{y}")
            if x == 0 or y == 0 or x == len(lines[0]) - 2 or y == len(lines) - 1: #check if on a vertical edge
                #print(f"[DEBUG] current tree is on an edge: {current_tree_height}")
                visable_trees += 1
            else:
                #print(f"[DEBUG] current tree: {current_tree_height}")
                #get left, right, up, down
                #left = lines[y][:x]
                #right = lines[y][x:len(lines[0]) - 1]
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
            print(f"current tree coord: {current_coord[0]},{current_coord[1]}")
            current_tree_height = int(lines[y][x])
            print(f"current tree height: {current_tree_height}")
            left = rows[y][:x]
            right = rows[y][x+1:]
            up = cols[x][:y]
            down = cols[x][y+1:]
            edge = False
            if x == 0 or y == 0 or x == len(lines[0]) - 2 or y == len(lines) - 1:
                edge = True
            current_scenic_score = scenic_score(current_tree_height, edge, left, right, up, down)
            print(f"[DEBUG] current scenic score: {current_scenic_score}")
            if current_scenic_score  > best_scenic_score:
                best_scenic_score = current_scenic_score
                best_coord[0] = current_coord[0]
                best_coord[1] = current_coord[1]
            print("-------------")
    print(f"[DEBUG] Part 2 best scenic score : {best_scenic_score} at coord {best_coord}")

def scenic_score(current_tree, edge: bool, left: str, right: list, up: list, down: list):
    if edge:
        print(f"[DEBUG] edge")
        return 0
    left_score = 0
    right_score = 0
    up_score = 0
    down_score = 0
    print(f"[DEBUG] left: {left}")
    print(f"[DEBUG] right: {right}")
    print(f"[DEBUG] up: {up}")
    print(f"[DEBUG] down: {down}")

    print(left[::-1])
    left = left[::-1]
    for x in left:
        if current_tree > int(x):
            print(f"[DEBUG] next left that can be seen: {int(x)}")
            left_score += 1
        else:
            print(f"[DEBUG] next left that can be seen: {int(x)}")
            left_score += 1
            break

    #for x in range(0,len(left)):
    #    if current_tree > int(left[x]):
    #        print(f"[DEBUG] next left that can be seen: {int(left[x])}")
    #        left_score += 1
    #    else:
    #        break
    for x in right:
        if current_tree > int(x):
            print(f"[DEBUG] next right that can be seen: {int(x)}")
            right_score += 1
        else:
            print(f"[DEBUG] next right that can be seen: {int(x)}")
            right_score += 1
            break

    #for x in range(0,len(right)):
    #    if current_tree > int(right[x]):
    #        #print(f"[DEBUG] next right that can be seen: {x}")
    #        right_score += 1
    #    else:
    #        break
    print(up[::-1])
    up = up[::-1]
    for x in up:
        if current_tree > int(x):
            print(f"[DEBUG] next up that can be seen: {int(x)}")
            up_score += 1
        else:
            print(f"[DEBUG] next up that can be seen: {int(x)}")
            up_score += 1
            break
    #try:
    #    up.reverse()
    #except AttributeError as zero_length:
    #    pass
    #for x in range(0,len(up)):
    #    if current_tree > int(up[x]):
    #        up_score += 1
    #    else:
    #        break
    for x in down:
        if current_tree > int(x):
            print(f"[DEBUG] next down that can be seen: {int(x)}")
            down_score += 1
        else:
            print(f"[DEBUG] next down that can be seen: {int(x)}")
            down_score += 1
            break
    #for x in range(0,len(down)):
    #    if current_tree > int(down[x]):
    #        down_score += 1
    #    else:
    #        break
    
    print(f"[DEBUG] {left_score} {right_score} {up_score} {down_score}")
    return left_score * right_score * up_score * down_score

def check_if_tree_is_higher(current_tree, left, right, up, down):
    if current_tree > max(left) or current_tree > max(right) or current_tree > max(up) or current_tree > max(down):
        return True
    else:
        return False

if __name__ == "__main__":
    main(sys.argv[1])