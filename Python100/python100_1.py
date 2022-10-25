# 문제 1 : 리스트의 삭제
# 다음 리스트에서 400, 500을 삭제하는 code를 입력하세요

nums = [100, 200, 300, 400, 500]

nums.pop(3)
nums.pop(3)
print(nums)

# 문제 2 : 리스트의 내장함수
# <pass> 부분에 리스트 내장함수 insert를 이용하여 코드를 입력하고 다음과 같이 출력되게 하세요

l = [200, 100, 300]
l.insert(2, 10000) # <pass> 
print(l)

# 문제 3 : 변수의 타입
# 다음 출력 값으로 올바른 것은?

l = [100, 200, 300]
print(type(l))

# 1. str 2. int 3. list 4. tuple
# 정답  : 3번

# 문제 4 : 변수의 타입2
# 다음 변수 a를 print(type(a))로 넣었을 때 출력될 값과의 연결이 알맞지 않은 것은?

# 1) 입력 : a=1, 출력 : class 'int'
# 2) 입력 : a=2.22, 출력 : class 'float'
# 3) 입력 : a='p', 출력 : class 'char'
# 4) 입력 : a=[1,2,3], 출력 : class 'list'

# 문제5 : for문 계산
# 다음 코드의 출력 값으로 알맞은 것은?

a = 10
b = 2
for i in range(1,5,2):
    a+=i
print(a+b)

# 답 : 16

# 문제6 : False
# 다음은 파이썬 문법 중에서 False로 취급하는 것들 입니다
# False로 취급하지 않는 True를 찾아주세요
# 1) None, 2) 1, 3) "", 4) 0, 5) bool(0)
# 답 : 2번

# 문제7 : 변수명
# 다음 중 변수명으로 사용할 수 없는 것 2개를 고르시오
# 1) age, 2) a, 3) as, 4) _age, 5) 1age
# 답 : 3,5 --> as는 키워드로 사용되기 때문에 사용 못함

# 문제8 : 딕셔너리 키 이름 중복
# 딕셔너리를 다음과 같이 만들었다. 출력값을 입력하시오

d = {'height':180, 'weight':78, 'weight':84, 'temparture':36, 'eyesight':1}
print(d['weight'])

# 답 : 84 -> 뒤에 입력된 값으로 덮어씌어짐

# 문제9 : sep와 end를 활용한 출력방법

year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

# 출력 -> 2019/04/26 11:34:27


# 문제10 : 별 찍기
# 크리스마스 날, 은비는 친구들과 함께 파티를 하기로 했습니다. 그런데, 크리스마스 트리를
# 사는 것을 깜빡하고 말았습니다. 온 가게를 돌아다녀 봤지만 크리스마스 트리는 모두 품절이었습니다.
# 하는 수 없이 은비는 프로그래밍으로 트리를 만들기로 합니다

# 입출력 예시
# >>입력 -> 5
# >>출력 -> *
#         ***
#        *****
#       *******
#      *********

inputNum = int(input())
for i in range(inputNum+1):
    print(" "*(inputNum-i) + (2*i-1) * '*')