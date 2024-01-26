"""
# H.w No. 1: # Create a Python function to calculate the area of a rectangle given its length and width as parameters
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Example usage:
length = 5
width = 10
print('Length = ', length, 'width = ', width
      ,"Area of rectangle:", calculate_rectangle_area(length, width))
"""
"""
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage:
word = "radar"
print(word, "is a palindrome?", is_palindrome(word))
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
num = 17
print(num, "is a prime number?", is_prime(num))