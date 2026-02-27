#exercise 8
#task 3
def first_n(items,n):
    result = []
    for i in range (n):
        result.append(items[i])
    return result
def test_first_n():
    assert first_n([10,20,30,40],2)==[10,20]
    assert first_n([1,2,3],1)==[1]
    assert first_n([5,6,7],3)==[5,6,7]
    print('test first_n: all passed')
test_first_n()
       
    