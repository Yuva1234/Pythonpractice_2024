Int = 1234
print(Int)
Flo = 3.25
print(Flo)
Compl = 6j
print(Compl)

## STRING ##
var1 = "Yuva"
var2 = "Maithri"
print(var1 + var2)
print(var2[0:3])   ## Indexing ##
print(var2[4])     
print(var2[0:5])   ## The indexing always follows var2[0:n-1] i.e var2[0:5 -1] therefore it gives index 0 to index 4. ##


str1 ="Chikile"
str2 = "YuvaMaithri"
print(f"My name is {str1} {str2}") ## F-string ##

alp1 = "abcdefghikl"
print(alp1[0:6])
print(alp1[:5])
print(alp1[2:])
print(alp1[:-1]) ## negative indexing gives the values from last ##
print(alp1[:-3])

print(alp1.replace("c", "u")) ## You replace alphabet 'c' with 'u' ## 

## Tuples/ A sequence of immmutable python obejects ##

mygrp = ('y' ,'u', 'v', 'a')
mygrp += ('f' , )       ## Concatenation of f to mygrp ##
print(mygrp)

weeks =('Sun', 'Mon','Tue','Wed','Thu','Fri', 'Sat', 'Sun')
print(type(weeks))  ## Type labels the type of data type ##




f1 = float(input("Enter the f1 : "))
f2 = float(input("Enter the f2 : "))
sum = f1 + f2
print(f"The sum of {f1} and {f2} is {sum} \n")




