def sum_evens ( numbers ) :
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print ( sum_evens ([1 , 2 , 3 , 4 , 5 , 6]) )
# Expected : 12 (2 + 4 + 6)
# Actual : 9