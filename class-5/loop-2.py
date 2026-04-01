# Fibonacci -> 0 1 1 2 3 5 8 13 21 34 55 ...
last = 1
secondLast = 1
i = 3
result = 0
while i < 11:
    result = last + secondLast
    secondLast = last
    last = result
    i = i + 1

print(result)
