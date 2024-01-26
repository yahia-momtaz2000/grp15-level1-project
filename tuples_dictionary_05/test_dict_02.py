# show dictionary basic
# Create dict
print('-----------  Create dict ------------------')
shopping_cart_dict = {'milk': 48.0, 'bread': 10.0, 'eggs': 145.0}
print(shopping_cart_dict)
print(type(shopping_cart_dict))

print('------------- Access element by Key ----------------')
print('value of key bread = ', shopping_cart_dict['bread']  )

print('----------------- Modify value of key ---------------')
shopping_cart_dict['bread'] = 15
print(shopping_cart_dict)

print('------------- Adding a new Key -------------------')
shopping_cart_dict['Nescafe'] = 60.0
print(shopping_cart_dict)

shopping_cart_dict['Nescafe'] = 69.0
print(shopping_cart_dict)

print('---------- Remove item from dict by key ----------------')
shopping_cart_dict.pop('Nescafe')
print(shopping_cart_dict)
shopping_cart_dict.popitem() # remove the last key
print(shopping_cart_dict)

print('------------- Concat between 2 dictionary ---------------')
dict1 = {101 : 'Ahmed', 102 :'Ola', 103:'Omar'}
dict2 = {104 : 'Ibrahim', 105 :'Sayed', 106:'Fathy'}

dict1.update(dict2)
print(dict1)






