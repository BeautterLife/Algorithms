def solution(array, commands):
    return [sorted(array[arr[0]-1:arr[1]])[arr[2]-1] for arr in commands]

