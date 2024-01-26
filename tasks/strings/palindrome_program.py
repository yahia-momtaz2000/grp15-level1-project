# H.w No. 5 # Develop a program that checks whether a given string is a palindrome or not.
# A palindrome is a string that reads the same forwards and backwards.

statement = ' 12521 '

if statement == statement[::-1]:
    print('it is a palind')
else:
    print('it is not a palind')