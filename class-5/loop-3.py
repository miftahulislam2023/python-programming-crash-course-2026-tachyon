# Prime -> 1, that number
i = 2
num = 611
flag = True
while i < num:
    if num % i == 0:
        flag = False
        print(i)
    i = i + 1

if flag:
    print("Prime")
else:
    print("Not prime")