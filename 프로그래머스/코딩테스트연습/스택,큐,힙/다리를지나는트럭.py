def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=[0]*bridge_length
    i=0
    while True:
        if sum(bridge[:-1]) + truck_weights[i] <= weight:
            bridge=[truck_weights[i]]+bridge[0:-1]
            answer+=1
            i+=1
            if i==len(truck_weights):
                answer+=bridge_length
                break
        else:
            for j,truck in enumerate(bridge[::-1]):
                if truck!=0:
                    j=int(j==0)+j
                    bridge=[0]*(j)+bridge[0:-j]
                    answer+=j
                    break
        
    return answer
