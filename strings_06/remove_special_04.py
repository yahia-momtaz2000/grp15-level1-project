# program to remove special characters from a string
statement = "123abcjw:, .@! eiw"
new_statement = ''
for letter in statement:
    if letter.isalnum():
        new_statement = new_statement + letter

print(new_statement)