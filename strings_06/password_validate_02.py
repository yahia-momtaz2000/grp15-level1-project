# program to validate password
"""
Minimum 8 characters.
At least one alphabet should be of Lower Case [a-z]	At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].		At least 1 character from [ _ or @ or $ ].
"""
password = "sr@m@_G0rtu9e$._2023"
count_upper, count_lower, count_digits, count_special = 0, 0, 0, 0
if len(password) >= 8:
    # then validate remaining points
    for letter in password:
        if letter.isupper():
            count_upper = count_upper + 1
        elif letter.islower():
            count_lower = count_lower + 1
        elif letter.isdigit():
            count_digits = count_digits + 1
        elif not letter.isalnum():
            count_special = count_special + 1
    if count_upper > 0 and count_lower > 0 and count_digits > 0 and count_special > 0:
        print('Password is valid and okay')
    else:
        print('Password is not Valid')
else:
    print('Password should be min 8 characters')
