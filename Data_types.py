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






## num1 = float(input("Enter first number : ")) ##
## num2 = float(input("Enter second number : ")) ##
## sum = num1 + num2 ##
## print(f"The sum of {num1} and {num2} is {sum} \n") ## 


## MUTABLE ##
## 1.LISTS - A sequence of mutable objects ##
mylist =["a","6a","name",9 ]
mylist += ["y"] ## CONCATENATION - The addition of values ##
print(mylist)

salaries = [10,20,30.1]


## Append ##
## salaries.append(6) ##
## print(salaries) ##


## CONCATENATION ##
salaries += ("abhi","junu","kali") ## CONCANTENATION of tuples to the list salaries ##
print(salaries) 

## Indexing ##
salaries[1] = 45
print(salaries)
print(type(salaries))

## 2.DICTIONERS ##
## An unordered collection of items ##
salary = {"Yuva":46000, "Maithri":50000, "Chikile":60000}
print(salary.get("Yuva"))
print(type(salary))
print(salary.get('Chikile')) 
print(salary["Yuva"])
print(salary.get("Maithri",44000)) ## assign the given value(44000) incase key has no value, but heer as the key i.e Maithri is already assigned you dont need 44000 ##
## 3.SETS ##
## Sets are immutable data types with no duplicate values ##
## Createa set ##
mySet ={1, 3, 5, 7, 9}
print(mySet)
print(type(mySet))
mySet.add(2)
print(mySet)
myS1 ={"anil" , "sunil" , "kapil"}
print(type(myS1))
print(myS1)
## print(myS1.pop(2))  ## As SETS is an unorder list of items. pop fuction cannot be used ##
print(mylist)
print(mylist.pop(3)) ## POP function is used to remove the elements in the list only ##
for x in mylist:
    print(x)            ## FOR LOOP ##

print(salary)
for x in salary.keys():
    print(x)
for x in salary.values():
    print(x)
for key,val in salary.items():
    print(key,val)

l1 =[]
for x in range(0, 10):
    l1.append(x)
print(l1)

## We can use COMPREHENSION FUNC for efficiency ##
l2=[x for x in range(0, 12)]
print(l2)

t1=tuple(x for x in range(1, 9))
print(t1)

s={x for x in range(0, 10)}
print(s)

d ={x: x*x for x in range(0, 10)}
print(d)
