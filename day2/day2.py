import sys

def main(input):
    lines = []
    with open(input) as file:
        lines = file.readlines()
        #print(lines)

    shape_point = {"X": 1, "Y": 2, "Z": 3} #A: rock, B: paper, C: scissor
    win_point = {"win": 6, "draw": 3, "loss": 0}

    for line in lines:
        print(f"[DEBUG] opponent: {line[0:1]} me: {line[2:3]}")

if __name__ == "__main__":
    main(sys.argv[1])