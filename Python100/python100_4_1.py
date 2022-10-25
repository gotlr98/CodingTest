# 문제 31 : 파이썬 자료형의 복잡도
# 다음 리스트의 내장함수의 시간 복잡도가 O(1)이 아닌것은?
# 1) l[i]
# 2) l.append(5)
# 3) l[a:b]
# 4) l.pop()
# 5) l.clear()
# 답 : 3번 --> 3번은 한번에 수행이 안되고 탐색을 2번해야한다


# 문제 32 : 문자열 만들기
# 취업 준비생인 혜림이는 자기소개서를 쓰고 있습니다. 열심히 자기소개서를 작성하던 도중 혜림이는 자기가 지금까지
# 단어를 얼마나 적었는지 궁금하게 됩니다.
# 혜림이를 위해 문자열을 입력받으면 단어의 갯수를 출력하는 프로그램을 작성해 주세요.
# 입력 : 안녕하세요. 저는 제주대학교 컴퓨터공학전공 혜림입니다.
# 출력 : 5

statement = input().split(' ')
print(len(statement))

# 답안 : 
# n = input() 
# l = list(n.strip().split())
# print(len(l))


# 문제 33 : 거꾸로 출력하기
# 한줄에 여러개의 숫자가 입력되면, 역순으로 그 숫자들을 하나씩 출력하는 프로그램을 작성

inputNum = list(input().split())
for i in range(len(inputNum)-1,-1,-1):
    print(inputNum[i], end=' ')
print('')

# 문제 34 : sort 확인하기

# 키가 주어지면 순서대로 제대로 섰는지 확인하는 프로그램을 작성해보자

# 입력 : 176 156 155 165 166 169
# 출력 : No

input_height = input()
n = list(map(int, input_height.strip().split()))

conv = sorted(n)
count = 0
for i in range(len(conv)):
    if conv[i] == n[i]:
        count += 1
if count == len(n):
    print('YES')
else:
    print('NO')


# 문제 35 : Factory 함수 사용하기
# 2제곱, 3제곱, 4제곱을 할 수 있는 Factory 함수를 만드려고 합니다

def one(n):
    def two(value):
        return value**n
            # <pass>
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))

#