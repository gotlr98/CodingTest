# 문제 41 : 소수판별
# 주어진 숫자가 소수면 YES로, 소수가 아니면 NO로 출력
# 에라토스테네스의 체 구현해보기

def check_prime(n):
    if n <= 1:
        return 'NO'
    i = 2
    prime = True
    while(i**2) < n:
        if n % i ==0:
            prime = False
            break
        i += 1
    if prime:
        return 'YES'
    else:
        return 'NO'

# 문제 42 : 요일 구하기
# 2020년 1월 1일은 수요일입니다. 2020년 a월 b일은 무슨 요일일까요?

import datetime 

month, day = map(int,input().split())

days = ['MON','TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

b = days[datetime.date(2020, month, day).weekday()]
print(b)


# 문제 43 : 10진수를 2진수로

digit = int(input())
b = []
i = 0
while True:
    if (digit < 2 ** i):
        b.append(str(digit%2))
        digit = digit // 2
        i = 0
    if (digit < 1):
        break
    i += 1
b.reverse()
print(''.join(b))

# 문제 44 : 각 자리수의 합

num = int(input())
b = []
while True:
    if num / 10 < 1:
        b.append(num)
        break
    
    b.append(num % 10)
    num = num // 10
    
print(sum(b))

# 문제 45 : time함수 사용하기

import time

t = time.time()
t = int(t//(3600*24*365)) + 1970
print(t)

# 문제 46 : str자료형의 응용
# 1부터 100까지의 모든 숫자를 일렬로 놓고 모든 자릿수의 총 합을 구하세요.

string = ''
sum = 0
for i in range(1, 101):
    string += str(i)

for i in string:
    sum += int(i)
print(sum)

# 문제 47 : set 자료형의 응용
# 중복된 데이터들을 삭제하여 실제 접수 명잔이 몇 명인지 알고 싶습니다

people = [
         ('이호준', '01050442903'),
         ('이호상', '01051442904'),
         ('이준호', '01050342904'),
         ('이호준', '01050442903'),
         ('이준', '01050412904'),
         ('이호', '01050443904'),
         ('이호준', '01050442903'),
         ]

print(len(set(people)))