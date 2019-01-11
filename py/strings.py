mystring = "a bcdefg"

#Slicing
print(mystring[2])
    #after third char
print(mystring[2:])
    #before third char (thirdchar not included)
print(mystring[:2])
    #middle slice (included)
print(mystring[2:5])
    #longkap 2
print(mystring[::2])

#Basic method
x = mystring.split()
print(x)

#Print Formatting
x = "Item One: {x} Item Two: {y}".format(x = "dog",y="cat")
print(x)
