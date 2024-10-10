print(" ")# print imprime un espacio

print("Sanchez Perez Briana Sarahi_1213_3W") 
print(" ")  # print imprime un espacio

def my_function(cantidad, pocentaje): # definiendo funcion

    iva = cantidad * (pocentaje / 100) # operacion de como sacar el iva
    total = cantidad + iva # operacion de total
    return total # total 

cantidad = float(input("Introduce la cantidad sin IVA: ")) # te pide que ingreses la cantidad 

porcentaje = float(input("Introduce el porcentaje de IVA: ")) # te pide que ingreses el porcentaje
porcentaje = 21 

factura = my_function(cantidad, porcentaje) # sacando factura 
print("El total de la factura es:", factura) # print imprime el total de la factura

print(" ") # print imprime un espacio