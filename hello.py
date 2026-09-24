def largest (numbers):
    largest = numbers[0]
    for item in numbers:
        if item > largest:
            largest = item
    return largest
result = largest([-3, -8, -1])
print(result) 

def second_largest (numbers):
    largest = numbers[0]
    second_largest = numbers[1] # Assumes numbers has at least 2 items, raises IndexError if thats not the case
    for item in numbers:
        if item > largest:
            second_largest = largest
            largest = item
        elif item > second_largest:
            second_largest = item
    return largest, second_largest
result = second_largest([-5,-8,6,4])
print(result)
         
