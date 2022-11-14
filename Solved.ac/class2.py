# 직사각형에서 탈출

# import math

# x, y, w, h = map(int, input().split())

# distance = []

# distance.append(abs(w-x))
# distance.append(abs(h-y))
# distance.append(abs(math.sqrt((y-x)**2 + (h-y)**2)))
# distance.append(abs(x))
# distance.append(abs(y))
# distance.append(abs(math.sqrt((y)**2 + (x)**2)))

# print(min(distance))

# 직각삼각형

while True:
    
    try:
        a = list(map(int, input().split()))

        if a[0] == 0 and a[1] == 0 and a[2] == 0:
            break
        else:
            a.sort()
            if a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
                print('right')
            else:
                print('wrong')
    except:
        break