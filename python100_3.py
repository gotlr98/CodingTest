# # 문제 21 : set은 어떻게 만드나요?
# # 다음 중 set을 만드는 방법이 아닌 것은?
# # 1) x={1,2,3,5,6,7}
# # 2) x={}
# # 3) x=set('python')
# # 4) x=set(range(5))
# # 5) x=set()

# # 답 : 2 --> 

# # 문제 22 : 배수인지 확인하기
# # 변수 i가 6의 배수인지 확인하는 코드를 짜시오

# # i % 6 == 0

# # 문제 23 : OX문제
# # print(10/2)의 출력 결과는 5이다 --> x 

# # 문제 24 : 대문자로 바꿔주세요!
# # 민지는 국제 포럼에서 아르바이트 하게 되었습니다. 민지는 각 국에서 온 참가자들의 명단을 엑셀로
# # 정리하고 있는데 참가자들 이름이 어떤 이는 전부 소문자, 어떤 이는 전부 대문자로 써져 있는 등 형식이
# # 제각각이었습니다. 민지를 위해 이름이 입력되면 전부 대문자로 출력되는 프로그램을 만들어주세요

# name = input()
# print(name.upper())


# # 문제 25 : 원의 넓이를 구하세요
# # 원의 넓이는 반지름의 길이 x 반지름의 길이 x 3.14 로 구할 수 있습니다.
# # 함수를 사용하여 원의 넓이를 구하는 코드를 작성해봅시다.

# # 입력을 반지름의 길이로 정수 n이 주어지면 원의 넓이를 반환하는 함수를 만들어 주세요.

# def get_cir(radius):
#     return (radius**2) * 3.14

# print(get_cir(int(input())))

# # 문제 26 : 행성 문제2
# # 우리 태양계를 이루는 행성은 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성이 있습니다
# # 이 행성들의 영어 이름은 Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus,
# # Neptune입니다.
# # 행성의 한글 이름을 입력하면 영어 이름을 반환하는 프로그램을 만들어 주세요.

# planet = {'수성' : 'Mercury',
#           '금성' : 'Venus',
#           '지구' : 'Earth',
#           '화성' : 'Mars',
#           '목성' : 'Jupiter',
#           '토성' : 'Saturn',
#           '천왕성' : 'Uranus',
#           '해왕성' : 'Neptune'}

# name = input()
# print(planet[name])

# # 문제 27 : 딕셔너리 만들기


# name = list(input().split())
# score = list(map(int, input().split()))

# empty = {name[0] : score[0],
#          name[1] : score[1]}

# # result = dict(zip(name, score))
# print(empty)


# # 문제 28 : 2-gram
# # 2-gram이란 문자열에서 2개의 연속된 요소를 출력하는 방법입니다.
# # 예를 들어 'Python'을 2-gram으로 반복해 본다면 다음과 같은 결과가 나옵니다
# # py
# # yt
# # th
# # ho
# # on

# two_gram = input()
# for i in range(len(two_gram)-1):
#     print(two_gram[i], two_gram[i+1], sep='')
# # 문제 29 : 대문자만 지나가세요
# # 알파벳을 여러개를 입력하고 여러개 입력한 것 중 대문자만 출력해주는 프로그램을 만들어라

# alphbet = input().split()

# for i in range(len(alphbet)):
#     if (alphbet[i].isupper()):
#         print(alphbet[i])

# 문제 30 : 문자열 속 문자 찾기
# 문자 pineapple에는 apple이라는 문자가 숨어 있습니다. 원범이는 이렇듯 문자열 속에 숨어있는
# 문자를 찾아보려고 합니다
# 입력으로 첫 줄에 문자열이 주어지고 둘째 줄에 찾을 문자가 주어지면
# 그 문자가 시작하는 index를 반환하는 프로그램을 만들어 주세요

statement = input()
findword = input()
find_num = 0
for i in range(len(statement)):
    if(statement[i:i+len(findword)] == findword):
        find_num = i
print(find_num)