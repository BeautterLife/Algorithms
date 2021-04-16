def list_count(input):
  input_set = set(input)
  
  if len(input_set)==1 or len(input_set)==len(input):
    return []
 
  input_dict = {num:input.count(num) for num in input_set}
  max_cnt = max(input_dict.values())
  
  return [num for num,cnt in input_dict.items() if cnt == max_cnt]


input = [1,1,1,2,2,2,2,3,4,5]
print(list_count(input))
