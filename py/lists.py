#Lists
##mylist = [1,2,3]
##mylist = ['stringadgasfd',1,2,3,23.2,True,'asdf',[1,2,3]]
mylist = ['a','b','c','d','e']
print('Before reassignment:')
print(mylist)
mylist[0] = 'NEW ITEM'
print('After reassignment:')
print(mylist)
mylist.append("NEW ITEM")
print('After appending:')
print(mylist)
mylist2=['x','y','z']
print('After extending with 2nd list:')
mylist.extend(mylist2)
print(mylist)
#LIST COMPREHENSION
#indexingindex
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print('ambil index kedua dari row kedua dari matrix:')
print(matrix[1][1])
first_col = [row[0] for row in matrix]
print(first_col)
