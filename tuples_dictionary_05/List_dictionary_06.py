# program to show a list of dictionaries
data_list = [  {7058: 'sravan', 7059: 'jyothika',  7072: 'harsha', 7075: 'deepika'}  ]

# display the list
print(data_list)
# display the first index of the list which is the whole dict
print(data_list[0])

# display data of key 7058
print(  data_list[0][7058]  )

# adding another dict to the list
data_list.append(  {7011: 'Hamad', 7012: 'Franshika'}  )
print(data_list[1][7011])

# update the value of dict of index 1 in the list with the key 7011
data_list[1][7011] = 'Ibraham'
print(data_list)
