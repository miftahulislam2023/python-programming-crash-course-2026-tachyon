# factorial
# 5! = 5 x 4 x 3 x 2 x 1
# 6! = 6 x 5 x 4 x 3 x 2 x 1

num = 6
result = 1
while num > 1:
    result = result * num
    num = num - 1 #decrement
print(result)