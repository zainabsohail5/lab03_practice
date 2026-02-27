def remove_negatives ( numbers ) :
    new_list=[]
    for num in numbers :
        if num>=0:
            new_list.append( num )
    return new_list

print ( remove_negatives ([1 , -2 , -3 , 4 , -5]) )
# Expected : [1 , 4]
# Actual : [1 , -3 , 4]