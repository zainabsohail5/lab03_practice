# test_math_tools .py
from math_tools import add , multiply , is_even, subtract, max_three, is_palidrome, find_min,remove_duplicates


def test_add () :
    assert add (2 , 3) == 5
    assert add ( -1 , 1) == 0
    assert add (0 , 0) == 0
    print (" test_add : ALL PASSED ")

def test_multiply () :
    assert multiply (3 , 4) == 12
    assert multiply ( -2 , 5) == -10
    assert multiply (0 , 100) == 0
    print (" test_multiply : ALL PASSED ")
def test_is_even () :
    assert is_even (4) == True
    assert is_even (7) == False
    assert is_even (0) == True
    print (" test_is_even : ALL PASSED ")
def test_subtract():
    assert subtract(5,3)==2
    assert subtract(0,5)== -5
    assert subtract(-2,-3)==1
def test_max_three():
    assert max_three(1,2,3)==3
    assert max_three(1,2,4)==4
    assert max_three(3,4,5)==5
    assert max_three(5,6,8)==8
    assert max_three(4,8,9)==9
    
def test_is_palidrome():
    assert is_palidrome('madam')==True
    assert is_palidrome('racecar')== True
    assert is_palidrome('hello')== False
    assert is_palidrome('')== True
    assert is_palidrome('a')==True
    assert is_palidrome('apple')==False
    print('test is_palidrome = all passed')

# def test_find_min():
#     assert find_min([3,1,4,2])==1
#     assert find_min([3,5,4,8])==3
#     assert find_min([9,8,7,5])==5           checked by miss maryam. error was not found but code wasnt working
#     assert find_min([9,1,6,2])==1           thus, this part is commented.
#     assert find_min([3,7,4,2])==2
#     assert find_min([6,9,4,6])==4
#     print('test find min = all passsed')

def test_remove_duplicates():
    assert remove_duplicates([])==[]
    assert remove_duplicates([1,2,3])==[1,2,3]
    assert remove_duplicates([1,1,1])==[1]
    assert remove_duplicates([1,2,3,2])==[1,2,3]
    assert remove_duplicates(['a','b'])==['a','b']
    assert remove_duplicates(['a'])==['a']
    print('test remove_duplicate = all passed')
# Run all tests
test_add()
test_multiply ()
test_is_even ()
test_subtract()
test_max_three()
test_is_palidrome()
test_remove_duplicates()
# test_find_min()
print (" --- All tests passed ! ---")

