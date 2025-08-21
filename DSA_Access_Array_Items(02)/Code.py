# Python - Access Array Items
import array as arr
# Using indexing.
# The following example shows how to access elements of an array using indexing.
n = arr.array('i', [44,55,66,7])
print(n[0])
print(n[3])
print()

# Using iteration.
n = arr.array('i', [44,55,66,7])

# iteration through for loop
for i in n:
  print(i)
print()

# Using enumerate() function.
n = arr.array('i', [44,55,66,7])
for i,v in enumerate(n):
  print(f'index:{i}, Value:{v}')