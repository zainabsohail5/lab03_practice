def add (a , b ):
    return a + b
def multiply (a , b ):
    return a * b
def is_even ( n ):
    return n % 2 == 0
def subtract(a,b):
    return a-b
def max_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
def is_palidrome(s):
    s = s.replace(" "," ")
    return s == s[::-1]

def find_min(num):
    min_value = num[0]
    
    for n in num:
        if n<min_value:
            min_value = n
    return min_value


def remove_duplicates(items):
    new_list=[]
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list