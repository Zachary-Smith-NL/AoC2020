def day_three(filename="input"):
    slope_sum = 0
    #first read in each line, stripping it of the newline character, and splitting down to the only tile that will be checked
    with open(filename, "r") as input_file:
        counter = 0
        for line in input_file:
            line = line.split("\n")[0]
            if(line[counter] == "#"):
                slope_sum += 1
            counter = (counter + 3) % len(line)
        print(slope_sum)

day_three()