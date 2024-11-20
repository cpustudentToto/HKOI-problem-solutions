num = input()

spaceBar = -1
i = 0
num1 = ""
num2 = ""

while i < len(num) and spaceBar == -1:
    if num[i] == " ":
        spaceBar = i
    i += 1

for i in range(spaceBar):
    num1 += num[i]
for i in range(spaceBar + 1, len(num)):
    num2 += num[i]

intNum1 = int(num1)
intNum2 = int(num2)
answer = intNum1 + intNum2
print(answer)