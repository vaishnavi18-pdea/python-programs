
def linear_search(roll_numbers, target):
    for index, roll_number in enumerate(roll_numbers):
        if roll_number == target:
            return index  
    return -1  
def sentinel_search(roll_numbers, target):
    n = len(roll_numbers)
    roll_numbers.append(target)  
    index = 0
    while roll_numbers[index] != target:
        index += 1
    roll_numbers.pop()
    return index if index < n else -1
roll_numbers = [101, 203, 304, 405, 506]
target = 304
print(roll_numbers)
print("Target: ", target)
linear_result = linear_search(roll_numbers, target)
print("Linear Search Result:", linear_result)
sentinel_result = sentinel_search(roll_numbers, target)
print("Sentinel Search Result:", sentinel_result)