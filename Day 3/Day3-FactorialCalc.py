'''
Day 3
Functions

Task : Factorial Calculator
Function Name : factorial
Input : Takes a number as an argument
Output : Factorial of a number n is the product of all positive integers less than or equal to n.

1. What is the simplest possible output?
f(0) = 0

2. Play ariund with an example and visualize.
f(0) = 0 return 1
f(1) = 1 --> 1
f(2) = 1 * 2 --> 2
f(3) = 1 * 2 * 3 --> 6
f(4) = 1 * 2 * 3 * 4 --> 24
f(5) = 1 * 2 * 3 * 4 * 5--> 120

we can summarize it to :
f(n) = f(n-1) * n

'''

# Trying recursive approach
def factorial_recursive(num) :
    if num == 0 :
        return 1
    else :
        return factorial_recursive(num-1) * num

def factorial_iterative(num) :
    result = 1
    for i in range (1,num+1) :
        result *= i
    return result

# Int as an input to calculate factorial
num = int(input("Insert number, we will calculate the factorial :"))
print(factorial_iterative(num))