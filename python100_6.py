# 문제 51 : merge sort를 만들어보자

def merge_sort(input_list):
    list_len = len(input_list)
    if list_len <= 1:
        return input_list
    mid_idx = list_len // 2
    list_one = merge_sort(input_list[:mid_idx])
    list_two = merge_sort(input_list[mid_idx:])

    result = []

    while list_one and list_two:
        if list_one[0] < list_two[0]:
            result.append(list_one.pop(0))
        else:
            result.append(list_two.pop(0))
    
    while list_one:
        result.append(list_one.pop(0))
    while list_two:
        result.append(list_two.pop(0))
    
    return result

giv_list = [180, 145, 165, 45, 170, 175, 173, 171]

print(merge_sort(giv_list))

# 문제 52 : quick sort

def quick_sort(input_list):
    list_len = len(input_list)
    if list_len <= 1:
        return input_list

    stand = input_list.pop(list_len//2)
    group_one = []
    group_two = []

    for i in range(list_len-1):
        if input_list[i] < stand:
            group_one.append(input_list[i])
        else:
            group_two.append(input_list[i])
    return quick_sort(group_one) + [stand] + quick_sort(group_two)
list = input().split(' ')
list = [int(i) for i in list]

print(quick_sort(list))

# 문제 53 : 괄호 문자열

def check_str(a):
    # print(a[::-1])
    len_a = len(a)
    if a[0] == ')':
        return 'NO'
    elif a[len_a-1] == '(':
        return 'NO'
    elif a.count('(') != a.count(')'):
        return 'NO'
    return 'YES'

a = input()
print(check_str(a))

# 문제 54 : 연속되는 수

num = list(map(int,input().split()))
num = sorted(num)
stand = num[1]-num[0]
for i in range(len(num)-1,1,-1):
    if (num[i]-num[i-1]) != stand:
        print('NO')
        break
print('YES')

# 문제 55 : 하노이

road = []
def hanoi(num, start, dest, layover):
    if num == 1:
        road.append([start, dest])
        return None
    hanoi(num-1, start, layover, dest)
    road.append([start, dest])
    hanoi(num-1, layover, dest, start)

user_input = int(input())
hanoi(user_input, 'A', 'C', 'B')
print(len(road))

# 문제 56 : 리스트의 함수 응용

nationWidth = {
    'korea' : 220877,
    'Rusia' : 17098242,
    'China' : 9596961,
    'France' : 543965,
    'Japan' : 377915,
    'England' : 242900
}

ver = nationWidth['korea']
diff = ver
key = ''
for i in nationWidth.keys():
    
    if i == 'korea':
        pass
    
    else:
        if abs(ver - nationWidth[i]) < diff:
            diff = abs(ver-nationWidth[i])
            key = i
print(key , diff)