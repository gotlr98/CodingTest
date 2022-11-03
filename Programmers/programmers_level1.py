# 짝수와 홀수

# def solution(num):
#     answer = ''
#     if num % 2 == 0:
#         answer += 'Even'
#     else:
#         answer += 'Odd'
#     return answer


# 평균 구하기

# def solution(arr):
#     answer = 0
#     answer = sum(arr) / len(arr)
#     return answer

# 약수의 합

# def solution(n):
#     answer = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             answer += i
#     return answer

# 자릿수 더하기

# def solution(n):
#     answer = 0

#     for i in range(len(str(n))):
#         answer += n % 10
#         n = n//10
#     return answer

# 신고 결과 받기

# def solution(id_list, report, k):
#     answer = []
#     for i in range(len(id_list)):
#         answer.append(0)
    
#     report_list = {}
#     for i in id_list:
#         report_list[i] = 0

#     report_history = []
#     for i in set(report):
#         report_list[i.split(' ')[1]] += 1
#         report_history.append(i)


#     report_name = []

#     for i in report_list:
#         if report_list[i] >= k:
#             report_name.append(i)

#     for j in report_history:
#         if j.split(' ')[1] in report_name:
#             answer[id_list.index(j.split(' ')[0])] += 1
#     return answer

# 숫자 짝꿍

# def solution(X, Y):
#     answer = ''

#     first_dict={}
#     second_dict={}
#     for i in range(0, 10):
#         first_dict[i] = 0

#     for j in range(0, 10):
#         second_dict[j] = 0

#     convX = list(X)
#     convY = list(Y)
    
#     for i in convX:
#         first_dict[int(i)] += 1
#     for j in convY:
#         second_dict[int(j)] += 1
#     a = []
#     b = []
#     for i in first_dict:
#         if first_dict[i] != 0:
#             a.append([i, first_dict[i]])
    
#     for i in second_dict:
#         if second_dict[i] != 0:
#             b.append([i, second_dict[i]])

    
#     print(a, b)

# 자연수 뒤집어 배열로 만들기

# def solution(n):
#     answer = []
#     # for i in range(str(n)):
#     #     answer.append(i[::-1])
#     for i in list(str(n)[::-1]):
#         answer.append(int(i))
#     return answer

# solution(12345)

# 정수 제곱근 판별

# import math

# def solution(n):
#     answer = 0
    
#     if int(math.sqrt(n)) == math.sqrt(n):
#         return (math.sqrt(n) + 1) ** 2
#     else:
#         return -1

# 문자열 내 p와 y의 개수

# def solution(s):
#     answer = True
    
#     s = s.lower()
    
#     if s.count('y') == s.count('p'):
#         return True

#     else:
#         return False

# 하샤드 수

# def solution(x):
#     answer = True
    
#     sum = 0
#     k = x
#     for i in range(len(str(x))):
#         sum += k % 10
#         k = k // 10
#     print(sum)
#     if x % sum == 0:
#         return True

#     else:
#         return False

# 문자열을 정수로 바꾸기

# def solution(s):
#     answer = 0

#     if s[0] == '-':
#         s = s[1:]
#         return -int(s)
#     elif s[0] == '-':
#         s = s[1:]
#         return int(s)
#     else:
#         return int(s)

# 나머지가 1이 되는 수 찾기

# def solution(n):
#     count = 1
    
#     while True:
#         if n % count == 1:
#             break
            
#         count += 1
#     return count

# def anonymize_text(sentences):
#     bef = sentences.split(' ')
#     result = ''
#     for i in bef:
#         if i[0].lower() != i[0]:
#             for j in i:
#                 result += 'X'
            
#         else:
#             result += i
#         result += ' '
                
#     return result[:-1]

# print(anonymize_text('John is old'))

# 정수 내림차순으로 배치하기

# def solution(n):
#     answer = ''
#     a = []
#     for i in str(n):
#         a.append(i)
#     a.sort(reverse=True)
#     print(a)
#     for i in a:
#         answer += i
#     return int(answer)

# x만큼 간격이 있는 n개의 숫자

# def solution(x, n):
#     answer = []
    
#     sum = x
#     for i in range(n):
#         answer.append(sum)
#         sum += x
#     return answer

# 콜라츠 추측

# def solution(num):
#     answer = 0
    
#     while True:
#         if num == 1:
#             return 0
#         else:
#             if num % 2 == 0:
#                 num /= 2
#             else:
#                 num = num * 3 + 1
#             answer += 1

#             if answer > 500:
#                 return -1
#             elif num == 1:
#                 return answer

# 두 정수 사이의 합

# def solution(a, b):
#     answer = 0
    
#     if a == b:
#         return a
#     else:
#         if a > b:
#             a, b = b, a
#         for i in range(a,b+1):
#             answer += i
#         return answer

# 서울에서 김서방 찾기

# def solution(seoul):
#     answer = ''
#     count = 0
#     for i in seoul:
#         if i == 'Kim':
#             break
#         count += 1
#     return '김서방은 ' + str(count) + '에 있다'

# 핸드폰 번호 가리기

# def solution(phone_number):
#     answer = ''
#     emp = phone_number[:-4]
#     back = phone_number[-4:]

#     for i in range(len(emp)):
#         answer += '*'
#     return answer + back

# 음양 더하기

# def solution(absolutes, sign):
#     answer = 0
#     count = 0
#     for i in sign:
#         if i == 'false':
#             absolutes[count] = -absolutes[count]
#         count += 1
#     print(absolutes)
#     return sum(absolutes)

# 없는 숫자 더하기

# def solution(num):
#     sum = 0
#     for i in range(10):
#         if i not in num:
#             sum += i

#     return sum

# 내적

# def solution(a, b):
#     count = 0
#     sum = 0
#     for i in a:
#         sum += i * b[count]
#         count += 1
#     return sum

# 나누어 떨어지는 숫자 배열

# def solution(arr, divisor):

#     answer = []

#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#     if len(answer) == 0:
#         answer.append(-1)
#     return sorted(answer)

# 제일 작은 수 제거하기

# def solution(arr):

#     target = min(arr)
#     arr.remove(target)
#     return arr

# 가운데 글자 가져오기

# def solution(s):

#     if len(s) % 2 == 0:
#         return s[(len(s)//2)-1] + s[(len(s)//2)]
#     else:
#         return s[len(s)//2]

# 수박수박수박수박수박수?

# def solution(n):
#     answer = ''
    
#     for i in range(n):
#         if i % 2 == 0:
#             answer += '수'
#         else:
#             answer += '박'
#     return answer

# 문자열 내림차순으로 배치하기

# def solution(s):
#     answer = ''
#     answer_ = []
#     answer__ = []
#     for i in s:
#         if i.lower() == i:
#             answer_.append(i)
#         else:
#             answer__.append(i)
    
#     for i in sorted(answer_, reverse=True):
#         answer += i
#     for j in sorted(answer__, reverse=True):
#         answer += j
        
#     return answer

# 문자열 다루기 기본

# def solution(s):
#     if len(s) == 4 or len(s) == 6:
#         for i in s:
#             if i.isdigit() == False:
#                 return False
#         return True
#     else:
#         return False

# 약수의 개수와 덧셈

# def solution(left, right):
#     count = 0
#     list = []
#     for i in range(left, right+1):
#         for j in range(1, i+1):
#             if i % j == 0:
#                 count += 1

#         if count % 2 == 0:
#             list.append(i)
#         else:
#             list.append(-i)
#         count = 0

#     return sum(list)

# 행렬의 덧셈

# def solution(arr1, arr2):
#     answer = []
    
#     for i in range(len(arr1)):
#         sum = []
#         for j in range(len(arr1[i])):
#             sum.append(arr1[i][j] + arr2[i][j])
#         answer.append(sum)
#     return answer

# 부족한 금액 계산하기

# def solution(price, money, count):

#     answer = 0
#     for i in range(count):

#         answer += price * (i+1)

#     if money - answer > 0 :
#         return 0
#     else:
#         return abs(answer-money)

# 직사각형 별찍기

# a, b = map(int, input().strip().split(' '))
# for i in range(b):
#     for j in range(a):
#         print('*', end='')
#     print('')

# 
import math

def solution(a,b):
    print('a')
    return(math.gcd(a,b),math.lcm(a,b))