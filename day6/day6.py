import sys

def charsInStringAreUnique(input_string):
    a=""
    for i in input_string:
        if i not in a:
            a+=i
    if(a==input_string):
        return True
    else:
        return False

def main(input):
    print("Start")
    lines = []
    with open(input) as file:
        lines = file.readlines()

    #lines = lines[:1]
    #parse string
    #get potential_buffer_start char and its position, put it into empty potential_buffer_list
    #take the following char and check if in potential_buffer_list
    #if yes: reset list, potential_buffer_start char is current potential_buffer_start + 1
    #if no: add following char to potential_buffer_list. 
    #if length of potential_buffer_list is 4: then te buffer is found
    example_string = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    potential_buffer_start_position = 0
    potential_buffer_list = ""
    potential_buffer_start_char  = ""

    example_string = lines[0]
    for pos in range(0,len(example_string)):
        print("new potential buffer list")
        potential_buffer_list = example_string[pos:pos + 14]
        if charsInStringAreUnique(potential_buffer_list):
            print(potential_buffer_list)
            print(pos + 14)
            break


    #potential_buffer_start_char = example_string[potential_buffer_start_position]
    #potential_buffer_list += potential_buffer_start_char

    #for pos in range(0,len(example_string)):
    #    potential_buffer_list = example_string[pos:pos + 4]
    #    print(potential_buffer_list)
    #    for potential_buffer_char in potential_buffer_list:
    #        print(potential_buffer_char)
    #        if not potential_buffer_char in potential_buffer_list:
    #            break
    #        else:
    #            print(pos + 4)

    #for pos in range(0,len(example_string)):
    #    if not example_string[pos] in potential_buffer_list and len(potential_buffer_list) < 4:
    #        print("add example_string[pos] to potential_buffer_list")
    #        potential_buffer_list += example_string[pos]
    #    elif len(potential_buffer_list) == 4:
    #        print(pos + 4)
    #        print(potential_buffer_list)
    #        break
    #    else:
    #        potential_buffer_list = ""

    #print(potential_buffer_start_position + 4)
    #print(potential_buffer_list)

if __name__ == "__main__":
    main(sys.argv[1])
