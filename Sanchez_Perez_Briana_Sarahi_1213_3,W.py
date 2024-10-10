print(" ")# print imprime un espacio

print("Sanchez Perez Briana Sarahi_1213_3W") 
print(" ")  # print imprime un espacio

import math # contiene funciones matemáticas

def my_function(radio): # definiendo funcion
    area = math.pi * (radio ** 2) # calcula el área
    return area # devuelve el valor calculado del área.


def my_function(radio, altura): # define una funcion
    area_base = my_function(radio) # almacena el área de la base del cilindro
    volumen = area_base * altura # calcula el volumen
    return volumen # devuelve el valor calculado del volumen

radio = float(input("Introduce el radio del círculo: ")) 
# pide que introduzca un valor para el radio del círculo

area = my_function(radio) # almacena el área del círculo 
print("El área del círculo es:", area) # print imprime el área del círculo

altura = float(input("Introduce la altura del cilindro: ")) 
# pide que introduzca la altura del cilindro

volumen = my_function(radio, altura) # almacena el volumen del cilindro
print("El volumen del cilindro es:", volumen) # print imprime el volumen del cilindro

print(" ") # print imprime un espacio
