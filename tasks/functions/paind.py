def is_palindrome(s):
    # Compare the string with its reversed version
    return s == s[::-1]

# Test the function
string1 = "radar"
print(is_palindrome(string1))  # Output: True

string2 = "Hello"
print(is_palindrome(string2))  # Output: False