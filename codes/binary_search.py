def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while(first <= last):
    midpoint = (first + last) // 2

    if(list[midpoint] == target):
      return midpoint
    elif(list[midpoint] < target):
      first = midpoint + 1
    else:
      last = midpoint - 1

  return None

def verify(result):
  if(result == None):
    print("Target not found.")
  else:
    print("Target found at:", result)

numbers = range(0, 10000000)
result = binary_search(numbers, 10000001)
verify(result)

result = binary_search(numbers, 9999998)
verify(result)



