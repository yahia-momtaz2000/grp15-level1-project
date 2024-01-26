# here we will show strings functions with examples
print('--------- Create and printing strings ---------')
emp_name = 'Yahia Momtaz'
print(emp_name)
print(type(emp_name))

print('--------- upper(), lower() strings functions  -------------')
upper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(upper_emp_name)
print(lower_emp_name)

print('---------------- isupper(), islower(), isalpha() strings functions ------------------')
print(upper_emp_name.isupper())
print(lower_emp_name.islower())
print(upper_emp_name.isalpha())


print('-------------- endswith() string function ---------------')
file_path = 'c:/my_Documents/egypt.PDF'
file_path = file_path.lower()
if file_path.endswith('pdf'):
    print('It is abook')
elif file_path.endswith('jpg') or file_path.endswith('png'):
    print('It is image')
else:
    print('Unknown file type')

print('------------- startswith() string function ------- ')
emp_mobile = '+201274077377'
if emp_mobile.startswith('+20'):
    print('Egyptian Mobile')
elif emp_mobile.startswith('+966'):
    print('Saudi Mobile')
else:
    print('Unknown country code')

print('------------------ membership in  not in  --------------------')
emp_bio = 'Iam a programmer, Iam interested in C++, python, oracle, java'
if 'python' in emp_bio or 'java' in emp_bio:
    print('It is the target employee')
else:
    print('It is not the target employee')

print('--------------  count string function ----------------------')
emp_bio = 'Iam a programmer, Iam interested in python, C++, python, oracle, java, python'
print( emp_bio.count('python'))

print('----------- replace(), index(), slicing ( substring ) in string -------------')
emp_email = 'yahia.momtaz.hussein.mohamed@msn.com'
user_name = emp_email[0: emp_email.index('@') ]
domain_name = emp_email[emp_email.index('@') + 1 :   ]    # [ 5:]
emp_name = user_name.replace('.',' ')
print(user_name)
print(domain_name)
print(emp_name)

print('---------------- Loop over String letters using foreach ----------------')
for letter in emp_name:
    print(letter)

print('------------- split() function : Convert from String to list ( words ) ---------------')
words_list = emp_name.split()
print(words_list)
for item in words_list:
    print(item)

print('-------------- join() function : convert the list back to string with space as separator --------')
new_emp_name = ' '.join(words_list)
print(new_emp_name)

print('------- Self study : title(), swapcase() find() rfind() strip()... - Self study -----------')
