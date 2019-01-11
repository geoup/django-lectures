#Dictionaries
my_stuff = {'key1':123,'key2':'value2','key3':{'123':[1,2,'grabMe']}}
print(my_stuff['key3']['123'][2].upper())

#Replace or ADD value in SETS
food = {'bfast':'eggs','lunch':'pizza'}
food['lunch']='burger'
food['dinner']='pasta'
print(food)
