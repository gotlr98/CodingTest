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

# num = int(input())

# count = 1

# while True:

#     temp = count

#     for i in str(count):
#         temp += int(i)
    
#     if temp == num:
#         print(count)
#         break

#     if count > num:
#         print(0)
#         break

#     count += 1
#     temp = 0

# 벌집

# num = int(input())
# count = 0
# sum_num = 1

# while True:

#     sum_num = sum_num + 6 * count

#     if sum_num >= num:
#         print(count+1) 
#         break
    
#     if num == 1:
#         print(1)
#         break

#     count += 1

# 블랙잭

# count, limit = map(int, input().split())

# card = list(map(int, input().split()))

# result = []

# for i in range(len(card)-2):
#     for j in range(i+1, len(card)-1):
#         for k in range(j+1, len(card)):
#             if (card[i] + card[j] + card[k]) <= limit:
#                 result.append(card[i] + card[j] + card[k])
#             else:
#                 pass

# print(max(result))

# Hashing

# num = int(input())
# alpha = input()

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# dict = {}
# count = 1
# for i in alphabet:
#     dict[i] = count
#     count += 1

# count_ = 0
# sum = 0
# for i in alpha:

#     sum += (dict[i] * (31 ** count_))
#     count_ += 1
# print(sum%1234567891)

# 팰린드롬수

# while True:

#     num = int(input())
#     if num == 0:
#         break
#     else:
#         if str(num) == str(num)[::-1]:
#             print('yes')
#         else:
#             print('no')

# 최대공약수와 최소공배수

import math

num1, num2 = map(int,input().split())

print(math.gcd(num1, num2))
print(math.lcm(num1, num2))