def isSorted(input):
  isUp = isDown = True
  
  previous = input[0]
  for num in input[1:]:
    if isUp:
      isUp = previous <= num
      
    if isDown:
      isDown = previous >=num
      
    if not(isUp or isDown):
        return False
    
    previous = num
  
  return True

print(isSorted([1,2,3,4,5]))
print(isSorted([1,2,3,4,5,3]))
print(isSorted([5,4,3,2,1]))
print(isSorted([3,5,4,3,2,1]))
    
