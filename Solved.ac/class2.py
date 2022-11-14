# 직사각형에서 탈출

import math

x, y, w, h = map(int, input().split())

distance = []

distance.append(abs(w-x))
distance.append(abs(h-y))
distance.append(abs(math.sqrt((y-x)**2 + (h-y)**2)))
distance.append(abs(x))
distance.append(abs(y))
distance.append(abs(math.sqrt((y)**2 + (x)**2)))

print(min(distance))