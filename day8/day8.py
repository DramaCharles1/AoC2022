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
                
    
    print("------------")
    for col in cols:
        print(col)
    

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
    print(f"line len {len(lines[0])}")
    print("------------")
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0]) - 1):
            current_tree_height = lines[y][x]
            print(f"current tree coord: {x},{y}")
            if x == 0 or y == 0 or x == len(lines[0]) - 2 or y == len(lines) - 1: #check if on a vertical edge
                print(f"[DEBUG] current tree is on an edge: {current_tree_height}")
                visable_trees += 1
            else:
                print(f"[DEBUG] current tree: {current_tree_height}")
                #get left, right, up, down
                #left = lines[y][:x]
                #right = lines[y][x:len(lines[0]) - 1]
                left = rows[y][:x]
                right = rows[y][x+1:]
                up = cols[x][:y]
                down = cols[x][y+1:]
                print(f"[DEBUG] left: {left}")
                print(f"[DEBUG] right: {right}")
                print(f"[DEBUG] up: {up}")
                print(f"[DEBUG] down: {down}")
                if check_if_tree_is_higher(current_tree_height, left, right, down, up):
                    visable_trees += 1
        print("------------")
    print(f"[DEBUG] visable trees: {visable_trees}")

    print(check_if_tree_is_higher(5,[2],[5,1,2],[0],[5,3,3]))

def check_if_tree_is_higher(current_tree, left, right, up, down):
    if current_tree > max(left) or current_tree > max(right) or current_tree > max(up) or current_tree > max(down):
        return True
    else:
        return False

if __name__ == "__main__":
    main(sys.argv[1])