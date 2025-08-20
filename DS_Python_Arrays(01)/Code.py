# Python Array ----- Multiple Example 
import array as arr

# creating an array with integer type
n = arr.array('i',[3,4,5,6]) # convert this list item is array
print(type(n),n)
print()

# creating an array with char type
a = arr.array('u','BAT')
print(type(a), a)
print()

# creating an array with float type
n = arr.array('d', [4.4, 45.4, 33.4])
print(type(n), n)
print()

# Accessing Array Element index item showing.
n = arr.array('i',[3,4,5,6])
print(n[3])
print(n[0])
print()

# Insertion Operation
n = arr.array('i',[3,4,5,6])
n.insert(0,9)
for i in n:
  print(i)
print()

# Deletion Operation
n = arr.array('i',[3,4,5,6])
n.remove(3)
for i in n:
  print(i)
print()

# Search Operation
n = arr.array('i',[3,4,5,6])
print(n.index(5))
print()

# Update Operation
n = arr.array('i',[3,4,5,6])
n[3] = 40
for i in n:
  print(i)