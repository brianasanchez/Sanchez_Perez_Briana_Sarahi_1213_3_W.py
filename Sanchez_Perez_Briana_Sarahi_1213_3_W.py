print(" ") # print imprime un espacio

print("Sanchez Perez Briana Sarahi_1213_3W") 
print(" ") # print imprime un espacio

def my_function(f): # defiendo funcion

    factorial = 1 # dando valor a variable
    for i in range(1, f + 1): 
        factorial *= i 
    return factorial # 


numero = int(input("Introduce un entero positivo: ")) # pide que ingreses un numero entero positivo

if numero < 0: # numero es mayor que 0
    print("Por favor, introduce un entero positivo.") # print imprimiendo texto
else: # se ejecuta si es falso
    resultado = my_function(numero) # sacando resultado
    print("EL resultado de", numero, "es:", resultado)# print imprimiendo resultado
    # print imprimiendo resultado

print(" ") # print imprime un espacio