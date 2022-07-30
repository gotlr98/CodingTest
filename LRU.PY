def LRU(cacheSize, cities):
    '''
    deque  자료형을 사용해서도 풀수 있다
    '''
    answer = 0
    
    cache_list=['']*cacheSize # 이 작업을 해주지 않으면 처음에 배열이 차있지 않아서 pop이 안된다
    
    if cacheSize == 0:
        answer = 5 * len(cities)
    
    else:
#         for i in range(cacheSize):
#             if cities[i] in cache_list:
#                 answer += 1
#                 cache_list.append(cities[0].lower())
#                 cities.pop(0)
#             else:
#                 cache_list.append(cities[0].lower())
#                 cities.pop(0)
#                 answer += 5

        for i in cities:
            i = i.lower()
            if i in cache_list:
                answer += 1
                cache_list.remove(i)
                cache_list.append(i)
            else:
                answer += 5
                cache_list.pop(0)
                cache_list.append(i)
    return answer

LRU(3, ["A","B","A"])