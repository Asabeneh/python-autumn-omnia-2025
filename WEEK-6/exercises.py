# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return 'Not defined'
    f = 1 
    for i in range(1, n + 1):
        f = f * i 
    return f


# 3! = 3 * 2 * 1 => 6 +> 1 * 2 * 3
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(-3))
print(factorial(0))


 
 
    