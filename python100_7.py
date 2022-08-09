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

# 문제 62 : 20190923 출력
# 코드 내에 숫자가 없어야 한다.
# 파일 이름이나 경로를 사용해서는 안된다.
# 시간, 날짜 함수를 사용해서는 안된다
# 에러 번호 출력을 이용해서는 안된다.
# input을 이용해서는 안된다

