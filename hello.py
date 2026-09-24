def largest (numbers):
    cont = False
    largest = numbers[0]
    for item in numbers:
        if item > largest:
            largest = item
    return largest
result = largest([-3, -8, -1])
print(result)       
