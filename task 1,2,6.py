#ex 8

#task1 : print(square(5)) will print None because there is no return statement. type of bug: missing return bug

#task2 : it creates an infinite loop because n is never changed inside loop.
 
#task6
# Reproduce: Ran reverse_list and saw incorrect output
# Isolate: Stepped through debugger and saw extra swaps
# Hypothesize: Loop runs too many times
# Test: Changed loop to len(items)//2
# Verify: Ran tests again and got correct output