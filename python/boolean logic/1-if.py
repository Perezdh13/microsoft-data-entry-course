# ejecutar el codigo solo si se ejecuta una condicion
a = 97
b = 55
if a < b:
    print(b)

# en python se debe aplicar sangria al cuerpo de una instruccion if si no se ejecutara el codigo de manera normal

if a < 0:
    print(a) # esta funcion print depende del if ya que tiene una sangria y no se ejecutara porque no se cumple la condicion
print(b)   # esta otra sin embargo se ejecutara de manera normal ya que al no disponer de sangria no depende del if