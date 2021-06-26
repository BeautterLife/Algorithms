#from collections import defaultdict
# defaultdict 사용이유 : 존재하지 않는 key는 error 발생시키지 않고,
# 자료형의 default 값을 넣어줌  
def solution(cacheSize, cities):
    answer = 0
    
    # key : 단어 value : used time(작을 수록 최근)
    cache = dict()
    #cache_set = set()  =>  dict도 유일성 보장하는 자료구조이므로 set 필요없음
    time = 0
    for city in cities:
        # 캐시 크기 == 0 : 항상 cache miss
        if cacheSize==0:
            time+=5
            continue
        
        # 대소문자 구분 안하므로 소문자로 통일
        city = city.lower()
        
        # cache hit이면 time +=1
        if city in cache.keys():
            time+=1
            # used time = 1 로 갱신해줌
            cache[city]=1
            # 사용되지 않은 단어는 used_time +=1
            for item in cache.keys():
                if item!=city:
                    cache[item]+=1
            continue
        
        # cache miss인데, cache full이면 
        # cache 갱신
        cache_renew =  True if len(cache) == cacheSize else False

        # 가장 큰 used time(사용된지 오래된)인 key를 cache에서 제거후
        # 현재 city를 caching
        max_time = 0  

        for key,value in cache.items():
            # 현재 cache에 있는 것들 used time +=1
            cache[key]+=1
            # cache 갱신해야하면 가장 큰 used time 항목의 key를 저장
            if cache_renew and max_time < value+1:
                max_time = value+1
                remove_key = key
        # cache 갱신해야하면 cache에서 제거
        if cache_renew:
            #cache_set.remove(remove_key)
            del cache[remove_key]
        
        # 현재 city를 caching함.
        cache[city] = 1
        # cache miss이므로 time+=5
        time +=5
        
        #cache_set.add(city)

    return time
