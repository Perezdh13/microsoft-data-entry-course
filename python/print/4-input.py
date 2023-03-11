# otra forma de pasar datos al programa es hacer que el usuario los ingrese. Puede codificarlo para que el programa le diga al usuario que ingrese la informacion, guarde los datos en el programa y luego actue en consecuecia.

print ("Welcome to the greeter program")
name = input("enter your name: ")
print("Greeetings " + name)

# la funcion input() almacena un reustado como un string por lo que el siguiente codigo no suma numero sino que concatena los string

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print("resultado suma: " + first_number + second_number)

# para resolverlo hay que convertir el valor del input (String) en in integral de la siguiente manera

print("resultado correcto")
print(int(first_number) + int(second_number))

# recuperamos el codigo del programa para la conversion de parsecs a años luz pero lo hacemos reutilizable añadiendo un input

parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")