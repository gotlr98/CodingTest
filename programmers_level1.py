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

def solution(id_list, report, k):
    answer = []
    for i in range(len(id_list)):
        answer.append(0)
    
    report_list = {}
    for i in id_list:
        report_list[i] = 0

    report_history = []
    for i in report:
        if i not in report_history:
            report_list[i.split(' ')[1]] += 1
        report_history.append(i)
    
    print(report_history)
    print(report_list)

    report_name = []

    for i in report_list:
        if report_list[i] >= k:
            report_name.append(i)

    for j in report_history:
        if j.split(' ')[1] in report_name:
            answer[id_list.index(j.split(' ')[0])] += 1
    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
