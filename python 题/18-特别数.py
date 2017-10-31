import math

num = 0
while True:
    sq1 = math.sqrt(num+100)
    sq2 = math.sqrt(num+268)

    flo1 = int(str(sq1).split('.')[1])
    flo2 = int(str(sq2).split('.')[1])

    if not flo1 and not flo2:
        break

    num += 1

print(num)