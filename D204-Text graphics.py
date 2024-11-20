#defining variables
runCode = True

#inputing the number
N = int(input())

#checking if a valid number was inputted
if N < 1 or N > 79:
    print("please input a number within the range of 1 - 79 inclusive")
    runCode = False
if N % 2 != 1:
    print("please input an odd number")
    runCode = False

#preparation of loop
if runCode:
    firstPound = int((N // 2) + 1)
    secondPound = 0

    #running the first half of the loop
    for k in range(1, (N // 2) + 1 + 1):
        for i in range(1, firstPound):
            print(" ", end = "")
        if k == 1:
            print("#")
        if k != 1:
            print("#", end = "")
            for i in range(secondPound - 1):
                print(" ", end = "")
            print("#")
        firstPound -= 1
        secondPound += 2
    
    #running the second half of the loop
    for k in range(1, (N // 2) + 1):
        firstPound += 1
        secondPound -= 2
        for i in range(1, firstPound + 1):
            print(" ", end = "")
        print("#", end = "")
        for i in range(secondPound - 1 - 1 - 1):
            print(" ", end = "")
        if k != (N // 2):
            print("#")