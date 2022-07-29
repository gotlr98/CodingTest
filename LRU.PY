def LRU(cacheSize, cities):
    answer = 0
    
    cache_list=['']*cacheSize
    
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