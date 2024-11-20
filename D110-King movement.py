import math

files = ["a","b","c","d","e","f","g","h"]
ranks = ["1","2","3","4","5","6","7","8"]
startingSquare = input()
endingSquare = input()

startingFile = files.index(startingSquare[0])
endingFile = files.index(endingSquare[0])
startingRanks = ranks.index(startingSquare[1])
endingRanks = ranks.index(endingSquare[1])

fileDistance = abs(endingFile - startingFile)

ranksDistance = abs(startingRanks - endingRanks)

if fileDistance > ranksDistance:
    print(fileDistance)
else:
    print(ranksDistance)