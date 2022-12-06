import sys

def charsInStringAreUnique(input_string):
    temp_string = ""
    for i in input_string:
        if i not in temp_string:
            temp_string+=i
    return temp_string == input_string

def main(input):
    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()

    example_string = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    potential_buffer_list = ""
    buffer_message_length = 14 #part 1: 4, part 2: 14

    example_string = lines[0]
    for pos in range(0,len(example_string)):
        potential_buffer_list = example_string[pos:pos + buffer_message_length]
        if charsInStringAreUnique(potential_buffer_list):
            print(f"Buffer message: {potential_buffer_list}")
            print(pos + buffer_message_length)
            break

if __name__ == "__main__":
    main(sys.argv[1])
