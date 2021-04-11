def solution(expression):
    
    arr_plus_minus = prior_converter1(expression,'+')
    arr_plus_mult = arr_plus_minus.copy()
    arr_minus_plus = prior_converter1(expression,'-')
    arr_minus_mult = arr_minus_plus.copy()
    arr_mult_plus = prior_converter1(expression,'*')
    arr_mult_minus = arr_mult_plus.copy()

    arr = [prior_converter2(arr_plus_minus,'-'),prior_converter2(arr_plus_mult,'*'),prior_converter2(arr_minus_plus,'+'),prior_converter2(arr_minus_mult,'*'), prior_converter2(arr_mult_plus,'+'),prior_converter2(arr_mult_minus,'-')]

    arr_op = ['+','+','-','-','*','*']
    #answer=[]
    answer = 0
    
    for i,ex in enumerate(arr):
        #answer.append(abs(eval(arr_op[i].join(ex))))
        answer = max(abs(eval(arr_op[i].join(ex))))
    #return sorted(answer)[-1]
    return answer 

def prior_converter1(expression, operator1):
    return expression.split(operator1)


def prior_converter2(split_expression, operator2):
    split_expression3 = []
    
    for k,i in enumerate(split_expression):
        tmp = ''
        
        for j in i.split(operator2):
            tmp+=str(eval(j))+operator2

        split_expression3.append(str(eval(tmp[:-1])))

    return split_expression3


        
        
            
    
