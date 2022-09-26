from re import L


def solution(users, emoticons):
    answer = []
    return answer

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
users_conv = {}
emoticons_conv = {}

for i in range(len(users)):
    users_conv[i+1] = users[i]
for j in range(len(emoticons)):
    for k in users_conv:
        # print(int(users_conv[k][0]) / 100 * emoticons[j])
        if j+1 in emoticons_conv.keys():
            emoticons_conv[j+1].append(int(users_conv[k][0]) / 100 * emoticons[j+1])
            # pass
        else:
            emoticons_conv[j+1] = int(users_conv[k][0]) / 100 * emoticons[j]


print(emoticons_conv)