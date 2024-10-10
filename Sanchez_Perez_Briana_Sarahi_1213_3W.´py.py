print(" ") # print imprime un espacio

print("Sanchez Perez Briana Sarahi_1213_3W") 
print(" ") # print imprime un espacio

def my_function(): # definiendo funcion
    print("Hey amigos!") #print imprime un saludo

while True: # bucle while
    input("Presiona Enter para recibir un saludo... ") #al presionar enter se da otro saludo igual
    my_function() #saludo
    continuar = input("¿Quisiera otro saludo, si o no?") # pregunta si quieres un saludo mas
    if continuar.lower() != 'si': # si quieres otro saludo se imprime uno igual
        break # se cierra el bucle while

print(" ") # print imprime un espacio

