N = input()
lastDigit = N[len(N) - 1]
if lastDigit == 1:
  print(N + "st")
elif lastDigit == 2:
  print(N + "nd")
elif lastDigit == 3:
  print(N + "rd")
else:
  print(N + "th")