# Python - Add Array Items

# Using append() method
'''
To add a new element to an array, use the append() method. 
It accepts a single item as an argument and append it at 
the end of given array.
'''
import array as arr
n = arr.array('i',[77,33,44])
print(type(n), n)
n.append(50) #This date add to last element just call append keyword.
print(n)
print()

# Using insert() method
n = arr.array('i', [55,66,77])
print(n)
n.insert(2,100) #Data insert position base point..
print(n)
print()

# Using extend() method This parameter specifies an array or iterable.
n1 = arr.array('i', [1,2,3,4,5,6]) 
n2 = arr.array('i',[7,8,9])
n1.extend(n2)
print(n1)
