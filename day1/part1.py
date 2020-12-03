def day_one(filename="input"):
    with open(filename, "r") as input_file:
        values = []
        maximum_value = -1
        minimum_value = 2020 #There must be a value less than this in the list for the question to be solveable, so it is safe to set minimum to this
        for line in input_file:
            value = int(line.split("\n")[0])
            values.append(value)
            if value < minimum_value:
                minimum_value = value
            elif value > maximum_value:
                maximum_value = value

        #Now I have a list of all of the values
        #First prune the list by removing values that cannot possibly be involved in a correct answer
        #These values are ones where:
        # value + maximum_value < 2020
        # or
        # value + minimum_value > 2020
        for value in values:
            if(value + maximum_value < 2020):
                values.remove(value)
            elif(value + minimum_value > 2020):
                values.remove(value)

        #Now with a reduced list of values, sort the list
        values.sort()

        #With the sorted list, begin checking each value using a binary-search-like method. Check the center of the list, if value + center < 2020, only check top half
        for value in values:
            result = checker(value, values)
            if result != None:
                return result
        
def checker(value, values):
    if(len(values) == 1):
        if value + values[0] == 2020:
            return value * values[0]
        else:
            return None
    else:
        toReturn = None
        midpoint = len(values) // 2
        value_check = values[midpoint]
        if value + value_check == 2020:
            toReturn = value * value_check
        elif value + value_check > 2020:
            toReturn = checker(value, values[:midpoint])
        elif value + value_check < 2020:
            toReturn = checker(value, values[midpoint:])
        return toReturn

def main():
    result = day_one()
    print(result)

main()