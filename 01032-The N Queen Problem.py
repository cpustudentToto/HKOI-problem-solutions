#If the remainder from dividing n by 6 is not 2 or 3 then the list is simply all even numbers followed by all odd numbers not greater than n.
#Otherwise, write separate lists of even and odd numbers (2, 4, 6, 8 – 1, 3, 5, 7).
#If the remainder is 2, swap 1 and 3 in odd list and move 5 to the end (3, 1, 7, 5).
#If the remainder is 3, move 2 to the end of even list and 1,3 to the end of odd list (4, 6, 8, 2 – 5, 7, 9, 1, 3).
#Append odd list to the even list and place queens in the rows given by these numbers, from left to right (a2, b4, c6, d8, e3, f1, g7, h5).

#General solution from "Eight queens puzzle. (2024, November 11). In Wikipedia. https://en.wikipedia.org/wiki/Eight_queens_puzzle"

N = int(input())

oddList = []
evenList = []
queensRankList = []

for i in range(1, N + 1, 2):
    oddList += [i]
    if i + 1 > N:
        break
    evenList += [i + 1]

if N % 6 == 2:
    oddList[0], oddList[1] = oddList[1], oddList[0]
    oddList.remove(5)
    oddList.append(5)

if N % 6 == 3:
    evenList.remove(2)
    evenList.append(2)
    oddList.remove(3)
    oddList.remove(1)
    oddList.append(1)
    oddList.append(3)

for i in evenList:
    queensRankList.append(i)
for i in oddList:
    queensRankList.append(i)

#output
for i in range(N):
    print(i + 1, queensRankList[i])