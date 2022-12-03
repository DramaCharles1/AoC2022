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

    outcome_map={
        "win": {"A": "Y",
                "B": "Z",
                "C": "X"},
        "draw": {"A": "X",
                "B": "Y",
                "C": "Z"},
        "loss": {"A": "Z",
                "B": "X",
                "C": "Y"}
    }

    score = 0
    part_2_score = 0
    for line in lines:
        temp_case = line[0:3]
        temp_shape = line[2:3]
        temp_opponent_shape = line[0:1]
        score = score + cases[temp_case] + shape_point[temp_shape]
        #Check if win/loose/draw
        if temp_shape == "X":
            part_2_score = part_2_score + 0 + shape_point[outcome_map["loss"][temp_opponent_shape]]
        if temp_shape == "Y":
            part_2_score = part_2_score + 3 + shape_point[outcome_map["draw"][temp_opponent_shape]]
        if temp_shape == "Z":
            part_2_score = part_2_score + 6 + shape_point[outcome_map["win"][temp_opponent_shape]]

    print(f"[DEBUG] total score: {score}")
    print(f"[DEBUG] total part 2 score: {part_2_score}")

if __name__ == "__main__":
    main(sys.argv[1])
