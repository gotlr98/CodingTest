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