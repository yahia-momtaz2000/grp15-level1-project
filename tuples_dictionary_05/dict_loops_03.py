# loop over dictionary [  ]
shopping_cart_dict = {'milk': 48.0, 'bread': 10.0, 'eggs': 145.0}
print('--------- 1- loop over keys [ for each ] -----------')
for key in shopping_cart_dict:
    print(key, shopping_cart_dict[key] )

print('-------- 2- loop over key, values ------------')
for key, value in shopping_cart_dict.items():
        print(key, value)

# Task : loop over all keys and raise the prices 10%
