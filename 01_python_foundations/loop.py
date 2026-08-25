£ While Loop
x = 1
while 11 > x:
    if x % 2 == 0:
        x += 1
        continue

    if x == 9:
        break

    print(x)
    x += 1