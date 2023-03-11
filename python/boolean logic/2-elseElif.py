# uso del else
a = 93
b = 27


if a < b:
    print(a) # como la condicion (if) no se cumple no se imprime esta linea
else:
    print(b) # entonces (else) imprime esta otra 

# uso del elif, se diferencia del else porque le da otra condicion al codigo antes de ejecutar

if a < b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")

# se pueden usar los tres elementos if, elif, else 

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")    

# un ejempli de logica condicional anidada seria el siguiente

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")
