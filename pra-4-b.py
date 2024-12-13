
def binary_search(roll_numbers, target):
    low, high = 0, len(roll_numbers) - 1
    while low <= high:
        mid = (low + high) // 2 
        if roll_numbers[mid] == target:
            return mid  
        elif roll_numbers[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  
    return -1  
def fibonacci_search(roll_numbers, target):
    n = len(roll_numbers)
    fib2, fib1 = 0, 1
    fibM = fib2 + fib1  
    while fibM < n:
        fib2, fib1 = fib1, fibM
        fibM = fib2 + fib1
    offset = -1
    while fibM > 1:
        i = min(offset + fib2, n - 1)
        if roll_numbers[i] < target:
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i
        elif roll_numbers[i] > target:
            fibM = fib2
            fib1 = fib1 - fib2
            fib2 = fibM - fib1
        else:
            return i
    if fib1 and offset + 1 < n and roll_numbers[offset + 1] == target:
        return offset + 1
    return -1  
roll_numbers = [101, 203, 304, 405, 506]
target = 304
print(roll_numbers)
print("Target: ", target)
binary_result = binary_search(roll_numbers, target)
print("Binary Search Result:", binary_result)
result = fibonacci_search(roll_numbers, target)
print("fibonacci_search:", result)