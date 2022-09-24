# def solution(today, terms, privacies):
#     today_conv = int(today.split('.')[0])
#     print(today_conv)
#     answer = []
#     return answer

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
privacies_conv = {}
terms_conv = {}
answer = []

today_conv = int(today.split('.')[0]) * 28 * 12 + int(today.split('.')[1]) * 28 + int(today.split('.')[2])


for i in terms:
    terms_conv[i.split(' ')[0]] = int(i.split(' ')[1])*28
count = 0
for j in privacies:
    
    if j.split(' ')[1] in privacies_conv:
        privacies_conv[j.split(' ')[1] + str(count)] = int(j.split(' ')[0].split('.')[0]) * 28 * 12 + int(j.split(' ')[0].split('.')[1]) * 28 + int(j.split(' ')[0].split('.')[2])
    else:
        privacies_conv[j.split(' ')[1]] = int(j.split(' ')[0].split('.')[0]) * 28 * 12 + int(j.split(' ')[0].split('.')[1]) * 28 + int(j.split(' ')[0].split('.')[2])
    count += 1
print(privacies_conv)

count_1 = 1

for k in privacies_conv:
    if today_conv - privacies_conv[k] >= terms_conv[k[0]]:
        answer.append(count_1)
    count_1 += 1

# print(answer)
