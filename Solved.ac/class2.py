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

# import math

# num1, num2 = map(int,input().split())

# print(math.gcd(num1, num2))
# print(math.lcm(num1, num2))

# 부녀회장이 될테야


# a = [[0 for col in range(15)] for row in range(15)]
# for i in range(15):
#     a[i][0] = 1
#     for j in range(14):
#         a[0][j] = j+1

# for i in range(1,15):
#     for j in range(1,15):
#         a[i][j] = a[i][j-1] + a[i-1][j]

# count = int(input())
# for i in range(count):
#     floor = int(input())
#     number = int(input())
#     print(a[floor][number-1])

# def count_num(floor, number):
    
#     result = 0
    
#     if floor == 0:
#         for i in range(number):
#             result += i+1
#         return result

#     else:
#         for i in range(number):
#             result += count_num(i-1, number)
#         return result

# count = int(input())
# for i in range(count):
#     floor = int(input())
#     number = int(input())
#     print(count_num(floor-1,number))

# 달팽이는 올라가고 싶다

# can, slip, meter = map(int, input().split())

# day = 1
# sum = 0
# while True:

#     sum += can
    
#     if sum >= meter:
#         print(day)
#         break

#     sum -= slip
#     day += 1

# a1 = can
# d = can - slip
# count = 0

# while True:

#     if ((count ** 2) * d) - (count * d) >= 2*meter:
#         print(count)
#         break

# if ((meter - a1 + d) / d).is_integer():
#     print(int((meter - a1 + d) / d))
# else:
#     print(int((meter - a1 + d) / d)+1)

#     break

#     count += 1

# 이항 계수 1

# import math

# n, k = map(int, input().split())

# print(int(math.factorial(n) / (math.factorial(n-k) * math.factorial(k))))
    
# 단어 정렬

# count = int(input())
# temp = []

# for i in range(count):
#     temp.append(input())

# temp = set(temp)
# range_list = sorted(temp, key = lambda x : (len(x), x))
# for i in range_list:
#     print(i)

# 영화감독 숌

# count = int(input())
# count_temp = 0
# # arr = []
# base = 0
# while True:
    
#     # for i in range(len(str(base))-2):
#     #     if str(base)[i] == '6' and str(base)[i+1] == '6' and str(base)[i+2] == '6':
#     #         count_temp += 1
#     #         continue
#     if str(base).find('666') != -1:
#         count_temp += 1
#         arr.append(base)
            
#     if count_temp == count:
#         print(base)
#         break
#     # if len(arr) == 10000:
#     #     break
#     base += 1

# 소수 찾기

# import math

# def primenumber(x):
#     for i in range(2, int(math.sqrt(x)+1)):
#         if x % i == 0:
#             return False
#     return True
# num = int(input())
# find = list(map(int, input().split()))
# find_num = 0

# for i in find:
#     if i <= 1:
#         pass
#     elif primenumber(i):
#         find_num += 1
# print(find_num)

# 덩치

num = int(input())

weight = []
height = []


for i in range(num):
    a, b = map(int, input().split())
    weight.append(a)
    height.append(b)

rank = [1] * len(weight)

for i in range(len(weight)-1):
    for j in range(i, len(weight)):
        if weight[i] < weight[j] and height[i] < height[j]:
            rank[i] += 1
print(rank)