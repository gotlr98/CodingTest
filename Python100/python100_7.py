# # 문제 61 : 문자열 압축하기
# # aaabbbbcdddd
# # 출력 : a3b4c1d4

# a = input()
# output = ''
# prev = a[0]
# count = 1
# for i in range(1, len(a)):
    
#     if prev != a[i]:
#         output =  output + (a[i-1] + str(count))
#         count = 0
    
#     count += 1
#     prev = a[i]
#     if i == len(a)-1:
#         output = output + (a[i-1] + str(count))
    
# print(output)

# # 문제 62 : 20190923 출력
# # 코드 내에 숫자가 없어야 한다.
# # 파일 이름이나 경로를 사용해서는 안된다.
# # 시간, 날짜 함수를 사용해서는 안된다
# # 에러 번호 출력을 이용해서는 안된다.
# # input을 이용해서는 안된다


# # 문제 63 : 친해지고 싶어
# # 입력이 주어지면 앞글자만 줄여 출력하기

# string = input().split()

# for i in string:
#     print(i[0], end='')

# # 문제 64 : 이상한 엘레베이터
# # 정량 N에 정확히 맞춰야만 움직이는 화물용 엘레베이터가 있다
# # 화물은 7kg, 3kg 두 가지이며 팔이 아픈 은후는 가장 적게 화물을 옮기고 싶습니다.
# # 예를 들어 정량이 24kg이라면 3kg 8개를 옮기는 것 보다는
# # 7kg 3개, 3kg 1개 즉 4개로 더 적게 옮길 수 있습니다.
# # 입력 : 정량 N이 입력
# # 출력 : 가장 적게 옮길 수 있는 횟수 출력, 만약 정량N이 되지 않으면 -1

# n = int(input())
# result = []
# count_7 = 0
# count_3 = 0

# # if (n % 3 != 0) or (n % 7 != 0) or (n % 21 != 0):
# #     result = -1

# for i in range(n):
#     for j in range(n):
#         if (7*i) + (3*j) == n:
#             result.append(i+j)

# if len(result) == 0:
#     print(-1)
# else:
#     print(min(result))

# # 문제 65 : 변형된 리스트
# # a = [1,2,3,4]
# # b = [a,b,c,d]
# # 출력 : [[1,a],[b,2],[3,c],[d,4]]

# a = [1,2,3,4]
# b = ['a','b','c','d']
# count = 0
# for i in a:
    
#     if i % 2 == 0:
#         print([b[count],i])
#     else:
#         print([i,b[count]])

#     count += 1

# 문제 66 : 블럭탑쌓기
# 입력
# 탑 = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BDEFG']
# 규칙 = 'ABD'
# 출력 = ['가능','불가능','가능','가능']

# from itertools import combinations

# top = input().split(',')
# rule = input()

# rule_conv = []
# conv = []
# result = ''

# for i in range(1, len(rule)):
#     rule_conv.append(zip(combinations(rule, i+1)))

# count = 0
# for t in top:
#     for a in t:
#         if a in rule:
#             result += a
#     if len(result) > 0:
#         conv.append(result)
#         result = ''


# for i in conv:
#     if len(i) == 1:
#         for j in range(len(rule)):
#             if rule[j] == i:
#                 print('가능', end='')
#                 continue
#     else:
#         print(1)

# 문제 67 : 민규의 악수
# 민규는 몇명의 사람들과 악수를 진행하는데 행사에서 진행된 악수횟수가 주어지면
# 민규가 악수한 횟수와 행사참가자를 출력하라

# shake = int(input())
# attend_num = 1
# while True:
#     if ((attend_num) * (attend_num-1) / 2) > shake:
#         break
#     attend_num += 1

# shake_minkyu = int(shake - ((attend_num-1) * (attend_num-2) / 2))

# print([shake_minkyu, attend_num])

# 문제 68 ; 버스 시간표
# 버스 시간표와 현재시간이 입력으로 주어지면 남은 시간을 출력하시오

# table = input().split(',')
# time = input()
# conv_time = int(time.split(':')[0]) * 60 + int(time.split(':')[1])

# for i in range(len(table)):
#     table[i] = int(table[i].split(':')[0]) * 60 + int(table[i].split(':')[1])

# for i in table:
#     if conv_time - i > 0:
#         print('지나갔습니다', end=' ')
#     else:
#         print(str(abs(conv_time-i)//60).zfill(2) + '시간' + str(abs(conv_time-i)%60).zfill(2) + '분', end=' ')

# 문제 69 : 골드바흐의 추측

# 2보다 큰 짝수 n이 주어졌을 때, 두개의 소수의 합으로 나타내라


# def era(n):
#     a = [False,False] + [True]*(n-1)
#     primes=[]

#     for i in range(2,n+1):
#         if a[i]:
#             primes.append(i)
#             for j in range(2*i, n+1, i):
#                 a[j] = False

#     return primes

# num = int(input())

# prime_list = era(num+1)
# result = []
# for i in prime_list:
#     for j in prime_list:
#         if (i+j) == num and [j,i] not in result:
#             result.append([i,j])
# print(result)

# 문제 70 : 행렬 곱
# 행렬 2개가 주어졌을 때 곱할 수 있는 행렬인지 확인하고 곱할 수 있다면 결과, 없다면 -1을 출력하라

a = ([1,2], 
    [2,4])
b = ([1,0],
    [0,3])

def solution(a, b):
    result = []
    k = 0
    if len(a[1]) == len(b[0]):
        for i in range(len(a)):
            for j in range(len(b)):
                for w in range(len(a[0])):
                    k+=a[i][j]*b[i][j]
                result.append(k)
            k=0
        print(result)
        return result

    else:
        return -1

solution(a,b)