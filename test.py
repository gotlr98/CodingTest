# num = int(input())
# b = []
# while True:
#     if num / 10 < 1:
#         b.append(num)
#         break
    
#     b.append(num % 10)
#     num = num // 10
    
# print(sum(b))

# print(int('a'))

import re

a = re.compile('[a-z]')
print(a.findall('abkdo239j'))
print(a.findall('zxk##$!)'))
print(a.findall('가나다라ldofo120##$'))
