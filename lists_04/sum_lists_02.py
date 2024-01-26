# program to sum the elements of a list
# using for i loop and for each loop

my_list = [15, 6, 2, 7 ,20]
print(my_list)
print('------ using for i loop -------')
v_sum = 0
for i in range(5):
    v_sum = v_sum + my_list[i]

print('sum = ', v_sum)

print('---------- using for each loop ------------')
v_sum = 0
for item in my_list:
    v_sum = v_sum + item

print('sum = ', v_sum)



print('----------- using sum general function -------------')
print(my_list)
print( sum(my_list) )
