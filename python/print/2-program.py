#funcion suma 
sum = 1 + 2
print(sum) 

#variables
product = sum * 2
print(product)

planets_in_solar_system = 8 # integer
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string
type(distance_to_alpha_centauri) ## <class 'float'>

from datetime import date #asi se importan modulos en este caso date

#print("Today's date is: " + date.today()) # esto devuelve un error 
print("Today's date is: " + str(date.today())) # hay que decir que date.today() va ser un string


#creando un convertidor de parsecs a años luz y convirtiendolo a string antes de imprimir en la consola
parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + "parsecs is " + str(lightyears) + "lightyears")

