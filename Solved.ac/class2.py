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

# while True:
    
#     try:
#         a = list(map(int, input().split()))

#         if a[0] == 0 and a[1] == 0 and a[2] == 0:
#             break
#         else:
#             a.sort()
#             if a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
#                 print('right')
#             else:
#                 print('wrong')
#     except:
#         break

# ACM 호텔

# count = int(input())
# answer = []
# temp = ''
# for i in range(count):
#     h, w, n = map(int, input().split())

#     if n % h == 0:
#         temp += str(h)
#     else:
#         temp += str(n % h)
    
#     if n % h == 0:
#         if len(str(n // h)) == 1 and n // h < 9:
#             temp += str('0') + str((n // h))
#         else:
#             temp += str((n // h))
#     else:
#         if len(str(n // h)) == 1 and n // h < 9:
#             temp += str('0') + str((n // h)+1)
#         else:
#             temp += str((n // h)+1)
#     answer.append(temp)
#     temp = ''

# for i in answer:
#     print(int(i))

# 분해합

num = int(input())

count = 1

while True:

    temp = count

    for i in str(count):
        temp += int(i)
    
    if temp == num:
        print(count)
        break

    if count > num:
        print(0)
        break

    count += 1
    temp = 0