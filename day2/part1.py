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
        char_range = [int(left_split[0].split("-")[0]), int(left_split[0].split("-")[1])] #Should now be an array of size 2, with the min and max of the specified character
        char = left_split[1]
        
        #Now all the required parts are arranged, check the password
        letter_counter = 0
        for letter in password:
            if(letter == char):
                letter_counter += 1
        if(letter_counter < char_range[0]):
            continue #Too few of the specified character, incorrect
        elif(letter_counter > char_range[1]):
            continue #Too many of the specified character, incorrect
        correct_counter += 1
    print(correct_counter)
    input_file.close()

day_two()
