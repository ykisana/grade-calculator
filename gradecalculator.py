def main():
    totalWeight = 0
    totalCalculated = 0

    running = True

    while running:
        weight = float(input("Enter weight of grade in percent: "))
        weight = (weight/100)
        totalWeight = totalWeight + weight
        grade = float(input("Enter value of grade in percent: "))
        calculated = grade*weight
        totalCalculated = totalCalculated + calculated
        print("%.2f" % totalCalculated/totalWeight)

        endProgram = input("End Program Y/N: ")
        if endProgram == "Y":
            running = False

def prompts(x):
    print("Select Funtion")
    print("1. Calculate New Grade")
    print("2. Continue Calculating Grade")
    print("3. Calculate Grade Needed to Pass")


main()




