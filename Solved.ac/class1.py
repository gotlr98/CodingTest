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

count = int(input())
a = []
b = []
for i in range(count):
    k,j = input().split()
    a.append(k)
    b.append(j)
m = 0
for i in b:
    for j in i:
        print(j*int(a[m]), end='')
    m += 1
    print()