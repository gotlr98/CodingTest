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

def solution(X, Y):
    answer = ''

    mid = ''
    count = 0
    for i in X:
        for j in Y:
            if i==j:
                mid += j
                Y = Y[:count] + Y[count+1:]
                print(Y)
            count += 1
        count = 0
    a = list(mid)
    for k in range(len(mid)):
        answer += max(a)
        a.remove(max(a))
    
    if answer == '':
        answer = '-1'
    answer = int(answer)
    
    return str(answer)

solution("5525", "1255")