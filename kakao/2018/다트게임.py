import math

pow_dic ={'S':1, 'D':2, 'T':3}

def solution(dartResult):
    process=[]
    num=''
    for a in dartResult:
        if a.isdigit():
            num+=a
        elif a.isalpha():
            process.append(power(int(num),a))
            num=''
        else:
            option(a,process)
            num=''

    return sum(process)

def power(num, n):
    return pow(num,pow_dic[n])

def option(opt,process):
    if opt=='#':
        process[-1]*=-1
    else:
        if len(process)>1:
            process[-2]*=2
        process[-1]*=2

            
