# testing loops
print('--------- for i loop -- print numbers from 1 to 10 -----------')
for i in range(1, 11):
    print(i, end=' ')

print('\n--------- for i loop -- print numbers from 1 to 10  step 2 -------')
for i in range(1, 11, 2):
    print(i, end=' ')

print('\n--- for i loop : Control statements - Continue,   break -------')
for i in range(1, 11):
    if i in (3, 5):   # if i == 3 or i == 5:
       continue
    elif i == 8:
        break
    print(i)

print('------------ Nested Loops : Multiplication table ----------------')
for i in range(1, 11):
    for j in range(1, 11):
        if i * j < 10:
            print(i * j, end='   ')
        else:
            print(i * j, end='  ')
    print('') # enter








