import sys

def main(input):
    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()

    shape_point = {"X": 1, "Y": 2, "Z": 3} #A: rock, B: paper, C: scissor
    win_point = {"win": 6, "draw": 3, "loss": 0}
    cases = {"A X": win_point["draw"],
             "A Y": win_point["win"],
             "A Z": win_point["loss"],
             "B X": win_point["loss"],
             "B Y": win_point["draw"],
             "B Z": win_point["win"],
             "C X": win_point["win"],
             "C Y": win_point["loss"],
             "C Z": win_point["draw"],}

    score = 0
    for line in lines:
        temp_case = line[0:3]
        temp_shape = line[2:3]
        #print(f"[DEBUG] outcome: {cases[temp_case]}")
        #print(f"[DEBUG] shape: {shape_point[temp_shape]}")
        score = score + cases[temp_case] + shape_point[temp_shape]

    print(f"[DEBUG] total score: {score}")

if __name__ == "__main__":
    main(sys.argv[1])