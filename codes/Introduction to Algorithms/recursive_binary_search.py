def recursive_binary_search(list, target):
  if(len(list) == 0):
    return False
  else:
    midpoint = (len(list)) // 2

    if(list[midpoint] == target):
      return True
    else:
      if(list[midpoint] < target):
        return recursive_binary_search(list[midpoint+1:], target)
      else:
        return recursive_binary_search(list[:midpoint-1], target)

def verify(result):
  if(result):
    print("Target found.")
  else:
    print("Target not found")

numbers = range(0, 10000000)
result = recursive_binary_search(numbers, 10000001)
verify(result)

result = recursive_binary_search(numbers, 3)
verify(result)