# 문제 11 : for 를 이용한 기본 활용
# 1부터 100까지 모두 더하는 Code를 <pass> 부분에 완성하세요

s = 0

for i in range(101): # <pass>
    s += i
print(s)

# 문제 12 : 게임 캐릭터 클래스 만들기
# 다음 소스코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '파이어볼'이 출력되게
# 만드시오. 주어진 소스 코드를 수정해선 안됩니다.

# <여기에 class 작성>

class Wizard:

    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')

x = Wizard(health = 545, mana=210, armor=10)
print(x.health, x.mana, x.armor)
x.attack()


# 문제 13 : 몇 번째 행성인가요?
# 우리 태양계를 이루고 있는 행성은 수성, 금성, 지구, 화성, 목성, 토성, 천왕성,
# 해왕성으로 총 8개 입니다. 저희는 우리 태양계의 n번째 행성이 무엇인지 알고 싶습니다
# 입력으로 행성의 순서를 나타내는 숫자 n이 입력됩니다
# 출력으로 그 순서에 해당하는 행성의 이름을 출력해 주세요

planet = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

count = int(input())

print(planet[count-1])

# 문제 14 : 3의 배수 인가요?
# 영희는 친구와 게임을 하고 있습니다. 서로 돌아가며 랜덤으로 숫자를 하나 말하고 그게
# 3의 배수이면 박스를 치고 아니면 그 숫자를 그대로 말하는 게임입니다
# 입력으로 랜덤한 숫자 n이 주어집니다.
# 만약 그 수가 3의 배수라면 '짝'이라는 글자를, 3의 배수가 아니라면 n을 그대로 출력

isMul = int(input())

if isMul % 3 == 0:
    print('짝')
else:
    print(isMul)


# 문제 15 : 자기소개
# 신학기가 시작되고, 아이들이 돌아가면서 자기소개를 하기로 했습니다
# 만약 입력으로 김다정 이라는 이름이 주어지면
# 안녕하세요. 저는 김다정입니다.
# 라고 출력하게 해주세요.

name = input()
print('안녕하세요. ' + '저는' + name+'입니다.')

# 문제 16 : 로꾸거
# 문장이 입력되면 거꾸로 출력하는 프로그램을 만들어 봅시다

i = input()


print(i[::-1])

# 문제 17 : 놀이기구 키 제한
# 유주는 놀이공원 아르바이트 중입니다. 그런데 놀이기구마다 키 제한이 있습니다
# 유주가 담당하는 놀이기구는 키가 150 이상만 탈 수 있습니다
# 입력으로 키가 주어지면
# 키가 150 이상이면 YES 틀리면 NO를 출력하는 프로그램을 작성하세요

height = int(input())

if height >= 150:
    print('YES')
elif height < 150:
    print('NO')


# 문제 18 : 평균 점수
# 영하네 반은 국어, 수학, 영어 시험을 보았습니다. 영하는 친구들의 평균 점수를
# 구해주기로 했습니다. 공백으로 구분하여 세 과목의 점수가 주어지면
# 전체 평균 점수를 구하는 프로그램을 작성하세요. 단, 소숫점 자리는 모두 버립니다

score1, score2, score3 = map(int, input().split())

print(int((score1+score2+score3)/3))
# 강사님 답 : data = list(map(int, input().split()))
# print(int(sum(data)/3))

# 문제 19 : 제곱을 구하자
# 공백으로 구분하여 두 숫자 a와 b가 주어지면, a의 b승을 구하는 프로그램을 작성

n = list(map(int, input().split()))
print(n[0] ** n[1])


# 문제 20 : 몫과 나머지
# 공백으로 구분하여 두 숫자가 주어집니다.
# 첫 번째 숫자로 두 번째 숫자를 나우었을 때 그 몫과 나머지를 공백으로 구분하여 출력

l = list(map(int, input().split()))
print(l[0] // l[1] + " " + l[0] % l[1])