def linear_search(list, target):
    """
    Return the position of target if found other wise return None
    """
    for i in range(0, len(list)):
        if(list[i] == target):
            return i
    return None

def verify(result):
    if(result == None):
        print("Target not found.")
    else:
        print("Target found at:", result)

numbers = range(0, 10000000)
result = linear_search(numbers, 10000001)
verify(result)

result = linear_search(numbers, 9999998)
verify(result)
