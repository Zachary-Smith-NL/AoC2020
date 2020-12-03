def day_three(filename="input"):
    slope_sum = []
    #first read in each line, stripping it of the newline character, and splitting down to the only tile that will be checked
    for i in range(5):
        slope_sum.append(0)
        input_file = open(filename, "r")
        lines = input_file.readlines()
        counter = 0
        if i == 4:
            down = 2
        else:
            down = 1
        right = (1 + (2 * i)) % 8
        for line_num in range(0, len(lines), down):
            line = lines[line_num].split("\n")[0]
            if(line[counter] == "#"):
                slope_sum[i] += 1
            counter = (counter + right) % len(line)
    slope_total = 1
    for value in slope_sum:
        slope_total *= value
    print(slope_total)

day_three()