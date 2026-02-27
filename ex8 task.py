#exercise 8
#task 4
def total_with_tax(price, rate):
    tax = price * rate
    total = price + tax
    return total
print(total_with_tax(100,0.15))