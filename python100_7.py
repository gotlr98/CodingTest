# 문제 61 : 문자열 압축하기
# aaabbbbcdddd
# 출력 : a3b4c1d4

a = input()
output = ''
prev = a[0]
count = 1
for i in range(1, len(a)):
    
    if prev != a[i]:
        output =  output + (a[i-1] + str(count))
        count = 0
    
    count += 1
    prev = a[i]
    if i == len(a)-1:
        output = output + (a[i-1] + str(count))
    
print(output)