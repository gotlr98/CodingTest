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


# 문제 63 : 친해지고 싶어
# 입력이 주어지면 앞글자만 줄여 출력하기

string = input().split()

for i in string:
    print(i[0], end='')

# 문제 64 : 이상한 엘레베이터
# 정량 N에 정확히 맞춰야만 움직이는 화물용 엘레베이터가 있다
# 화물은 7kg, 3kg 두 가지이며 팔이 아픈 은후는 가장 적게 화물을 옮기고 싶습니다.
# 예를 들어 정량이 24kg이라면 3kg 8개를 옮기는 것 보다는
# 7kg 3개, 3kg 1개 즉 4개로 더 적게 옮길 수 있습니다.
# 입력 : 정량 N이 입력
# 출력 : 가장 적게 옮길 수 있는 횟수 출력, 만약 정량N이 되지 않으면 -1

n = int(input())
result = []
count_7 = 0
count_3 = 0

# if (n % 3 != 0) or (n % 7 != 0) or (n % 21 != 0):
#     result = -1

for i in range(n):
    for j in range(n):
        if (7*i) + (3*j) == n:
            result.append(i+j)

if len(result) == 0:
    print(-1)
else:
    print(min(result))

# 문제 65 : 변형된 리스트
# a = [1,2,3,4]
# b = [a,b,c,d]
# 출력 : [[1,a],[b,2],[3,c],[d,4]]

a = [1,2,3,4]
b = ['a','b','c','d']
count = 0
for i in a:
    
    if i % 2 == 0:
        print([b[count],i])
    else:
        print([i,b[count]])

    count += 1