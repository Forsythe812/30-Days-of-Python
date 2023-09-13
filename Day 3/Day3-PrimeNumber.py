'''
Day 3
Functions

Task : Prime Checker
Function Name : is_prime
Input : Takes a number as an argument
Output : Return True if it's a prime, false otherwise

We check the divisibility of the given number N with all the numbers starting from 2 to (N/2). 
If it is completely divisible by any number i.e. remainder is zero after division, then the number is not a prime number. 
If it is not completely divisible by a number between 2 and (N/2), then the number is a prime number.

If n is not a prime, it can be written as n=a*b, where neither a nor b can be greater than sqrt(n) and both not lesser than it at the same time.
Why? Because if both a and b are greater than sqrt(n), then a*b would be greater than b, which is a contradiction. Similarly, if both a and b are less than sqrt(n), then a*b would be less than n.
Thus, at least one of the numbers a or b must be less than or equal to sqrt(n).
'''

#function is_prime, take int as an argument
def is_prime(num) :
    if (num <= 1) :
        return False
    for i in range (2,int(num**0.5)+1) : # We only need to check up to the square root of num 
        if (num % i == 0) :
            return False
    return True

# take int as an input
num = int(input("Insert number, we will check if it's a prime number :"))
print(is_prime(num))

# using test cases to automate testing
import random

for i in range (0,10) :
    rand_num = random.randint(0,100)
    if is_prime(rand_num) :
        print(f'The number {rand_num} is a Prime number')
    else :
        print(f'The number {rand_num} is NOT a Prime number')
