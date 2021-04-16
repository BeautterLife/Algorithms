def isSorted(input):
  isUp = isDown = True
  
  previous = input[0]
  for num in input[1:]:
    if isDown and num > previous:
      isDown = False
    if isUp and num < previous:
      isUp = False
    previous = num

    if not(isUp and isUp):
        return False
  
  return isUp or isDown

print(isSorted([1,2,3,4,5]))
print(isSorted([1,2,3,4,5,3]))
print(isSorted([5,4,3,2,1]))
print(isSorted([3,5,4,3,2,1]))
    
