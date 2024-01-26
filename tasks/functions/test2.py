# search for number in a list and return its index
def search(lst,n):
    if n in lst:
        x = lst.index(n)
    else:
        x = 'not found'
    return x
lst = [5,-1,6,9,7,-8]
n = 6
find_number = search(lst,n)
print('the index of the number is ',find_number)