# 단어의 개수

# sentence = input()
# if sentence == ' ':
#     print(0)
# else:
#     print(len((sentence.strip()).split(' ')))

# 단어 공부

# word = input().upper()

# count = {}
# for i in word:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# max_val = [k for k,v in count.items() if max(count.values()) == v]
# if len(max_val) > 1:
#     print('?')
# else:
#     print(max_val[0])

# 평균

# count = int(input())
# score = list(map(int,input().split()))
# conv_score = []

# for i in range(count):
#     conv_score.append(score[i] * 100/(max(score)))
# print(sum(conv_score)/len(score))

# 검증수

# num = list(map(int, input().split()))
# sum = 0
# for i in num:
#     sum += i**2
# print(sum%10)

# 문자열 반복

# count = int(input())
# a = []
# b = []
# for i in range(count):
#     k,j = input().split()
#     a.append(k)
#     b.append(j)
# m = 0
# for i in b:
#     for j in i:
#         print(j*int(a[m]), end='')
#     m += 1
#     print()

# 상수

# num1, num2 = input().split()

# num1, num2 = num1[::-1], num2[::-1]

# if int(num1) >= int(num2):
#     print(num1)
# else:
#     print(num2)

# 음계

# ap = list(map(int, input().split()))

# comp = sorted(ap)
# comp_ = sorted(ap, reverse=True)

# if ap == comp:
#     print('ascending')
# elif ap == comp_:
#     print('descending')
# else:
#     print('mixed')

# 나머지

# a = []
# for i in range(10):
#     temp = int(input())
#     a.append(temp%42)

# print(len(set(a)))

# OX퀴즈

# count = int(input())

# quiz = []
# for i in range(count):
#     quiz.append(input())

# sum = 0
# sa = 0
# count_ = 1
# for i in quiz:
#     for j in i:
#         if j == 'X':
#             sa = 0
        
#         elif j == 'O':
#             sa += 1
#             sum += sa

    
#     print(sum)
#     sum = 0
#     sa = 0

# 알파벳 찾기

# alpha = input()
# dict = {}
# a = 'abcdefghijklmnopqrstuvwxyz'

# for i in a:
#     dict[i] = -1

# for j in alpha:
#     dict[j] = alpha.index(j)

# for i in dict.values():
#     print(i, end=' ')

# 아스키 코드

# num = input()
# print(ord(num))

# a+b -4

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break