def day_one_2(filename="input"):
    with open(filename, "r") as input_file:
        #Less overengineering this time
        values = []
        for line in input_file:
            value = int(line.split("\n")[0])
            values.append(value)
        for value in values:
            for value2 in values:
                if value == value2:
                    continue
                for value3 in values:
                    if value == value3 or value2 == value3:
                        continue
                    if value + value2 + value3 == 2020:
                        #If values aren't the same & add up to 2020
                        print(value * value2 * value3)
                        return
day_one_2()