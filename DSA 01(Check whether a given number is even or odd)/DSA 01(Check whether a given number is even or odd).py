'''
Check whether a given number is even or odd ???

Approach: By Finding the Basic Remainder....?

Step ----------01-----------

'''
# Convert to num in int type !
num = int(input("Enter The First Number : "))

# Apply to condition and chack it's true or false.
if num % 2 == 0:
    print("Your type number Is",num,"it's Even Number")
    
else:
    print("Your type number Is",num,"it's Odd Number")




'''
Approach: By Finding the Remainder

Step-------------02--------------

'''
def is_even_odd(n):
    return (n % 2 == 0)
    
if __name__ == "__main__":
    n = int(input("Enter The Number :"))
    
    if is_even_odd(n):
        print("Your typing number Is",n,"it's Even Number")
    else:
        print("Your typing number Is",n,"it's Odd Number")




'''
Approach: Using Bitwise AND Operator

The last bit of all odd numbers is always 1, 
while for even numbers it’s 0. So, when performing bitwise 
AND operation with 1, odd numbers give 1, and even numbers 
give 0.


Step -----------------------03---------------------
'''

def Check_even_odd(n):
    if (n & 1) == 0:
        return True
    else:
        return False
        
if __name__ =="__main__":
    n = int(input("Enter The Number: "))
    
    if Check_even_odd(n):
        print("Your type number Is" ,n,"it's Even Number")
    else:
        print("Your type number Is",n,"it's Odd Number")
    

    


'''
Approach: Using Bitwise Shift Operators
Right shifting n >> 1 removes the last bit. Shifting back 
restores it. If the result matches the original number, 
it's even.

Step-----------------------04------------------------

'''

def chack_odd_even(n):
    if n == (n >> 1) << 1:
        return True
    else:
        return False
    
if __name__ == "__main__":
    n = int(input("Enter The Number: "))
    
    if chack_odd_even(n):
        print("Your typing number Is",n,"it's Even Number")
    else:
        print("Your typing number Is",n,"it's Odd Number")