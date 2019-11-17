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
        print(totalCalculated/totalWeight)

        endProgram = input("End Program Y/N: ")
        if endProgram == "Y":
            running = False



main()




