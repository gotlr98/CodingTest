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

# 최대공약수와 최소공배수

# def GCD(n,m):
#     while(m):
#         n,m = m,n%m
#     return n

# def LCM(n,m):
#     result = (n*m) // GCD(n,m)
#     return result

# def solution(n, m):
#     answer = []

#     answer.append(GCD(n,m))
#     answer.append(LCM(n,m))
            
#     return answer

# 같은 숫자는 싫어

# def solution(arr):
#     answer = []
    
#     answer.append(arr[0])
#     arr.remove(arr[0])
#     count = 0
#     for i in arr:
#         if i == answer[count]:
            
#             pass
#         else:
#             answer.append(i)
#             count+=1
#     return answer

# 이상한 문자 만들기

# def solution(s):
#     answer = ''
#     count = 0

#     for i in (s.lower()).split(' '):
#         for j in i:
#             if count % 2 == 0:
#                 answer += j.upper()
#             else:
#                 answer += j
#             count += 1
#         answer += ' '
#         count = 0
#     return answer[:-1]

# 3진법 뒤집기

# def solution(n):
#     answer = 0
#     a = ''
#     while(n):
#         a += str(n % 3)
#         n = n // 3
#     count = 0
#     for i in a[::-1]:
#         answer += int(i) * (3**count)
#         count += 1
#     return answer

# 예산

# def solution(d, budget):
#     result = 0

#     d.sort()
#     count = 0
#     for i in d:
#         if result + i > budget:
#             break
#         else:
#             result += i
#             count += 1
#     return count

# 시저암호

# def solution(s, n):
#     a = ''
#     for i in s:
#         if i == ' ':
#             a += ' '
#             pass
#         else:
#             if (ord(i)+n) >= 91:
#                 a += chr((ord(i)+n-26))
#             elif (ord(i)+n) >= 123:
#                 a += chr((ord(i)+n-26))
#             else:
#                 a += chr((ord(i)+n))
#     return a
# print(solution('a A z',25))

# 최소직사각형

# def solution(sizes):
#     conv = []
#     for i, j in sizes:
#         if i <= j:
#             conv.append([j,i])
#         else:
#             conv.append([i,j])
    
#     width = []
#     length = []
#     for i, j in conv:
#         width.append(i)
#         length.append(j)

#     return max(width) * max(length)

# # 문자열 내 마음대로 정렬하기

# def solution(strings, n):

    
#     strings.sort(key=lambda x : x[n])

#     for i in range(len(strings)-1):
#         for j in range(1, len(strings)):
#             if strings[i][n] == strings[j][n]:
#                 if strings[i] > strings[j]:
#                     strings[i], strings[j] = strings[j], strings[i]
#     return strings

# print(solution(["abce", "abcd", "cdx"], 2))
    
# K번째수

# def solution(array, commands):
#     answer = []
    
#     for i,j,k in commands:
#         temp = array[i-1:j]
#         temp.sort()
#         print(temp[k-1])
#         answer.append(temp[k-1])
#     return answer

# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 숫자 문자열과 영단어

# def solution(s):
#     answer = ''

#     dict = {}
#     temp = ''
#     alpha = ['zero', 'one', 'two', 'three','four', 'five',
#             'six', 'seven', 'eight', 'nine']
#     count = 0
#     for i in alpha:
#         dict[i] = count
#         count += 1

#     for i in s:
#         if i.isdigit():
#             answer += str(i)

#         else:
#             temp += i

#             if temp in dict.keys():
#                 answer += str(dict[temp])
#                 temp = ''
        
#     return int(answer)

# print(solution("23four5six7"))

# 삼총사

# def solution(number):

#     count = 0

#     for i in range(len(number)-2):
#         for j in range(i+1, len(number)-1):
#             for k in range(j+1, len(number)):
#                 if number[i] + number[j] + number[k] == 0:
#                     count += 1

#     return count

# print(solution([-2, 3, 0, 2, -5]))

# 두개 뽑아서 더하기

# def solution(numbers):
#     answer = []
    
#     for i in range(len(numbers)-1):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     answer.sort()
#     answer_ = list(set(answer))
#     answer_.sort()
#     return answer_

# 2016년

# from datetime import datetime

# def solution(a, b):
#     month, day = str(a), str(b)
#     if len(month) == 1:
#         month = '0'+month

#     date = '2016-' + month + '-' + day
#     datetime_date = datetime.strptime(date, '%Y-%m-%d')

#     dict_day = {}
#     st = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
#     for i in range(7):
#         dict_day[i] = st[i]

#     return dict_day[datetime_date.weekday()]

# print(solution(2, 29))

# 폰켓몬

# def solution(nums):

#     can = int(len(nums)//2)

#     varie = len(list(set(nums)))

#     if can < varie:
#         return can

#     elif varie < can:
#         return varie
    
#     else:
#         return can

# 모의고사

# def solution(answers):

#     one = [1,2,3,4,5]
#     two = [2,1,2,3,2,4,2,5]
#     three = [3,3,1,1,2,2,4,4,5,5]
#     answer = []
#     correct = []
#     corr_one = 0
#     corr_two = 0
#     corr_three = 0

#     for i in range(len(answers)):
#         if one[(i)%5] == answers[i]:
#             corr_one += 1
#         if two[(i)%8] == answers[i]:
#             corr_two += 1
#         if three[(i)%10] == answers[i]:
#             corr_three += 1

#     correct.append(corr_one)
#     correct.append(corr_two)
#     correct.append(corr_three)

#     for i in range(len(correct)):
#         if max(correct) == correct[i]:
#             answer.append(i+1)
#     return answer


#     # count_one = 1
#     # for i in range(len(answers)):
#     #     one.append(count_one)
#     #     count_one += 1
#     #     if count_one > 5:
#     #         count_one = 1
            

#     # count_two = 1
    
#     # for i in range(len(answers)):
#     #     if i % 2 == 0:
#     #         two.append(2)
            
#     #     else:
#     #         if count_two == 2:
#     #             count_two += 1
#     #             two.append(count_two)
#     #         else:
#     #             two.append(count_two)
#     #             count_two += 1
        
#     # count_three = [3,1,2,4,5]
#     # count_three_ = 0
#     # for i in range(len(answers)):
#     #     three.append(count_three[count_three_])
#     #     if i != 0 and i % 2 == 1:
#     #         count_three_ += 1

#     #     if count_three_ == 5 and i % 2 == 0:
#     #         count_three_ = 0


#     # a = 0

#     # for i in answers:
#     #     if one[a] == i:
#     #         corr_one += 1
#     #     if two[a] == i:
#     #         corr_two += 1
#     #     if three[a] == i:
#     #         corr_three += 1

#     #     a += 1
#     # print(one)
#     # print(two)
#     # print(three)

#     # first.append(corr_one)
#     # first.append(corr_two)
#     # first.append(corr_three)


    
# print(solution([1, 2, 3, 4, 5]))

    
# 소수 찾기

# import math

# def primenumber(n):
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# def solution(n):
#     answer = 0
    
#     for i in range(2, n+1):
#         if primenumber(i):
#             answer += 1
#     return answer

# def prime_list(n):  # 에라토스테네스의 체

#     sieve = [True] * n

#     m = int(n**0.5)

#     for i in range(2, m+1):
#         if seive[i]:
#             for j in range(i+i, n, i):
#                 sieve[j] = False

#     return [i for i in range(2, n) if sieve[i] == True]

# 소수 만들기

# import math

# def primenumber(n):
    
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# def solution(nums):
#     answer = 0
    
#     for i in range(len(nums)-2):
#         for j in range(i+1, len(nums)-1):
#             for k in range(j+1, len(nums)):
#                 if primenumber(nums[i]+nums[j]+nums[k]):
#                     answer += 1


#     return answer

# 콜라 문제

def solution(a, b, n):
    answer = 0

    while True:

        if n <= 1:
            break
        answer += (n // a) * b
        print(answer)
        n = n - n//a



    return answer

print(solution(2, 1, 20))