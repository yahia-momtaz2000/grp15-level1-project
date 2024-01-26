def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, n):
        if n % i == 0:
            return False  # If a factor is found, the number is not prime
    return True  # If no factors other than 1 and itself, it's a prime number

# Test the function
number1 = 17
print(is_prime(number1))  # Output: True

number2 = 4
print(is_prime(number2))  # Output: False