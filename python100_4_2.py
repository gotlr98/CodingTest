# 문제 36 : 구구단 출력하기
# 1~9까지의 숫자 중 하나를 입력하면 그 단의 구구단 결과를 한 줄에 출력하는 프로그램

inputNum = int(input())

for i in range(1, 10):
    print(inputNum * i, end=' ')
print('')

# 문제 37 : count 사용하기

# 학생들이 뽑은 후보들을 입력받으면 뽑힌 학생의 이름과 받은 표 수를 출력
# 다시 코딩해보기 어렵다..

data = input().split()
data_set = set(data)
data_dict = {}
for key in data_set:
    data_dict[key] = data.count(key)

print(f'{max(data_dict, key=data_dict.get)}(이)가 총 {max(data_dict.values())} 표로 반장이 되었습니다.')



# 문제 38 : 호준이의 아르바이트
# 호준이는 아르바이트로 영어 학원에서 단어 시험지를 채점하는 일을 하고 있다. 호준이가 일하는 학원은 매번 1위부터
# 3위까지의 학생에게 상으로 사탕을 준다. 그런데 오늘은 마침 사탕이 다 떨어져서 호준이가 채점을 하고 점수를 보내면,
# 당신이 아이들의 숫자만큼 사탕을 사러 가기로 했다.
# 학생들의 점수를 공백으로 구분하여 입력받는다. 1위 ~ 3위 학생은 여러명일 수 있고 1~3위 학생 중 중복되는 학생까지 
# 포함하여 사탕을 사기로 한다.
# 학생 수는 4명 이상입니다.
# 숫자 외에 다른 값은 입력되지 않습니다

input_num = list(map(int, input().split()))

count = 0
peo_count = 0
input_num_sort = sorted(input_num, reverse=True)
prev = input_num_sort[0]
for i in range(1,len(input_num_sort)):
    if peo_count == 3:
        break;
    if input_num_sort[i] != prev:
        prev = i
        peo_count += 1
    count += 1
print(count)


# 문제 39 : 문장이 입력되면 모든 q를 e로, b를 n으로 바꾸는 프로그램을 작성

statement = input()
statement=statement.replace('q', 'e')
statement=statement.replace('b', 'n')
print(statement)
    
# 문제 40 : 놀이동산에 가자

# 첫번째 줄에서 제한 무게가 주어지고 두번째 줄에서는 함께한 친구들의 수 n이 주어집니다
# 그 다음 차례대로 탑승할 친구들의 몸무게가 주어집니다. 몸무게는 무작위로 주어집니다

limit = int(input())
num_peo = int(input())
s_list = list(map(int,([input() for _ in range(num_peo)])))
accu = 0
for i in range(num_peo):
    accu += s_list[i]
    if accu > limit:
        break
print(i)


