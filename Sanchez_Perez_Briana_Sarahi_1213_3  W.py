print(" ") # print imprime un espacio

print("Sanchez Perez Briana Sarahi_1213_3W") 
print(" ") # print imprime un espacio

from functools import reduce # aplica una función de manera acumulativa

def my_function(lista): # definiendo funcion
    return reduce(lambda x, y: x + y, lista) # aplica una función lambda

def my_function(lista): # definiendo funcion
    return reduce(lambda x, y: x * y, lista) # 


numeros = [1, 2, 3, 4] # define una lista

suma = sum(numeros) # realiza suma
producto = my_function(numeros) # realiza operacion para sacar el producto

print("La suma de la lista es:", suma) # print imprime la suma de la lista
print("El producto de la lista es:", producto) # print imprime el producto de la lista

print(" ") # print imprime un espacio