a = 10
b = 20

#Relational Operators
print (a>b)#Greater | F
print(b<a)#Lesser   | F
print(a<=b)#Less or Equal | T
print(b>=a)#Greater or equal | T
print(a!=b)#Not equal | T
print(a == b-10)# equal | T

#Logical Operators
#And Or Not
#And - Both of the condition have be true for the expression to be true
#Or - One of the condition have be true for the expression to be true
# Not - Negate the condition

print()
a = 10
b = 5

print(a == b and b>a)#True
print(a+5 >= b or b>a)#true
print(not(a>b) or a<b)#false
print(not(not(b>a) and a>b))#true


