import sys
import itertools

def main(input):
    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()

    #[H]                 [Z]         [J]
    #[L]     [W] [B]     [G]         [R]
    #[R]     [G] [S]     [J] [H]     [Q]
    #[F]     [N] [T] [J] [P] [R]     [F]
    #[B]     [C] [M] [R] [Q] [F] [G] [P]
    #[C] [D] [F] [D] [D] [D] [T] [M] [G]
    #[J] [C] [J] [J] [C] [L] [Z] [V] [B]
    #[M] [Z] [H] [P] [N] [W] [P] [L] [C]
    # 1   2   3   4   5   6   7   8   9

    #.........Top.......................Bottom
    stack1 = ['H','L','R','F','B','C','J','M']
    stack2 = ['D','C','Z']
    stack3 = ['W','G','N','C','F','J','H']
    stack4 = ['B','S','T','M','D','J','P']
    stack5 = ['J','R','D','C','N']
    stack6 = ['Z','G','J','P','Q','D','L','W']
    stack7 = ['H','R','F','T','Z','P']
    stack8 = ['G','M','V','L']
    stack9 = ['J','R','Q','F','P','G','B','C']
    stack_map = [['x','x'], stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

    #lines = lines[:1]

    for line in lines:
        #print("----------------")
        nmbr_of_crates_to_move = int(line.split(" ")[1])
        from_stack = int(line.split(" ")[3])
        to_stack = int(line.split(" ")[5])
        #print(f"[DEBUG] nmbr_of_crates_to_move: {nmbr_of_crates_to_move}")
        #print(f"[DEBUG] from_stack: {from_stack}")
        #print(f"[DEBUG] to_stack: {to_stack}")
        #print(f"[DEBUG] old from_stack: {stack_map[from_stack]}")
        #print(f"[DEBUG] old to_stack: {stack_map[to_stack]}")
        temp_move = stack_map[from_stack][:nmbr_of_crates_to_move]
        #commen line underneath for part 2
        temp_move.reverse()
        #print(f"[DEBUG] stack to move: {temp_move}")
        stack_map[to_stack].insert(0,temp_move)
        stack_map[from_stack] = stack_map[from_stack][nmbr_of_crates_to_move:]
        stack_map[to_stack] = list(itertools.chain.from_iterable(stack_map[to_stack]))
        #print(f"[DEBUG] new from_tack: {stack_map[from_stack]}")
        #print(f"[DEBUG] new to_stack: {stack_map[to_stack]}")

    stack_str = ""
    for stack in stack_map:
        stack_str += stack[0]
    print(stack_str)
if __name__ == "__main__":
    main(sys.argv[1])
