# how to use lists in python
print('--------- Create new List -------------')
numbers_list = [15, 16, 40, 3, 10]
print(numbers_list)
print( type(numbers_list)  )

print('---------- adding new item _ append, insert -------------')
numbers_list.append(33)
numbers_list.insert(2, 17)
print(numbers_list)

print('----------- Access a specific element & change this element ------')
print(   numbers_list[3]    )
numbers_list[3] = 44
print(numbers_list)

print('-- count elements in the list - we use general function len ----------------')
print(  len(numbers_list)  )

print('----------- Looping on a List ---------------')
print(numbers_list)
print('------------- Using for i loop ( index ) ------------')
for i in range( 7 ):
    print( i, numbers_list[i]  )

print('-------- using for each loop ( for in loop ) -  ( not using index ) ----------')
for item in numbers_list:
    print(item)

print('------- using for each loop + manual index -----------------------')

i = 0
for item in numbers_list:
    print(i, item)
    i = i + 1


print('------------ Delete element from the list ---------')
print('Original list ', numbers_list)
print('------- using remove function ----------')
numbers_list.remove(16)
print(numbers_list)

print('------------ using pop function ---------------')
numbers_list.pop(4)
print(numbers_list)

print('--------- Reverse List -------------')
print('Original list ', numbers_list)
numbers_list.reverse()
print(numbers_list)

print('-------- Sorting list ------------')
numbers_list.sort()
numbers_list.sort( reverse= True)
print(numbers_list)
