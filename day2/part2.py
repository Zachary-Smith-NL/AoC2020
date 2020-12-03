def day_two(filename="input"):
    input_file = open(filename, "r")
    correct_counter = 0
    #First get both sides by splitting on the colon
    #Then split up the left side by " " to get the two parts of that
    #Finally split up the first part of the left side by "-" to get the min and max of the specified character
    for line in input_file:
        split_line = line.split(":")
        left_side = split_line[0]
        right_side = split_line[1]
        #Right side now will just be stripped of spaces and the newline character
        right_side = right_side.split("\n")[0]
        password = right_side.split(" ")[1]

        #Left side will be split again
        left_split = left_side.split(" ")
        char_indices = [int(left_split[0].split("-")[0]) - 1, int(left_split[0].split("-")[1]) - 1]
        char = left_split[1]

        #Now all the required parts are arranged, check the password
        char_indices[0] = password[char_indices[0]]
        char_indices[1] = password[char_indices[1]]
        if (char_indices[0] == char) ^ (char_indices[1] == char):
            correct_counter += 1


    print(correct_counter)

day_two()