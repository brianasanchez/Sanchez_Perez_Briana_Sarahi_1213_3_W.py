print(" ")# print imprime un espacio

print("Sanchez Perez Briana Sarahi_1213_3W") 
print(" ")  # print imprime un espacio

def my_function(cadena): # definiendo funcion
    cadena = cadena.strip() # elimina los espacios en blanco
    if not cadena: # evalúa si la cadena está vacía
        return 0  # si la cadena está vacía devuelve 0
    palabras = cadena.split() # divide la cadena en una lista de palabras
    ultima_palabra = palabras[-1] # accede a la última palabra en la lista
    longitud = len(ultima_palabra) # calcula la longitud de la última palabra
    return longitud # longitud de la última palabra

cadena = input("Introduce una cadena de texto: ") # solicita que introduzca una cadena de texto
longitud = my_function(cadena) # resultado de la función
print("La longitud de la última palabra es:", longitud) # print imprime la longitud de la ultima palabra

print(" ") # print imprime un espacio