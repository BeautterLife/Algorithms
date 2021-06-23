from collections import defaultdict
def solution(cacheSize, cities):

    cache = defaultdict()
    cache_set = set()
    time = 0
    
    for city in cities:
        if cacheSize==0:
            time+=5
            continue
            
        city = city.lower()
        
        if city in cache_set:
            time+=1
            cache[city]=1
            for item in cache_set:
                if item!=city:
                    cache[item]+=1
            continue
        
        is_cache_renew =  True if len(cache_set) == cacheSize and cacheSize>0 else False
   
        max_time = 0, 0 

        for key,value in cache.items():

            cache[key]+=1
            if is_cache_renew and max_time < value+1:
                max_time = value+1
                remove_key = key
        if is_cache_renew:
            cache_set.remove(remove_key)
            del cache[remove_key]    
        
        cache[city] = 1
        
        time +=5
        cache_set.add(city)

    return time
