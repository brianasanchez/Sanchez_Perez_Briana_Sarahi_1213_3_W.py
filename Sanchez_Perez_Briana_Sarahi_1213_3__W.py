print(" ") # print imprime un espacio

print("Sanchez Perez Briana Sarahi_1213_3W") 
print(" ") # print imprime un espacio

def my_function(email): # definiendo funcion
    if "@" in email: # comprueba si el símbolo "@" está presente en la cadena email
        return True # si la condición es verdadera entonces se da true
    else: # se ejecuta si la condición no se cumple
        return False # si la condición es falsa entonces se da false

email = input("Introduce tu dirección de correo electrónico: ") 
# solicita que introduzca una dirección de correo electrónico
 
if my_function(email): # si la función devuelve True el código dentro de if se ejecutará.
    print("La dirección de correo electrónico es válida.") # print imprime que la dirección de correo es válida.
else: # se ejecuta si es falso
    print("La dirección de correo electrónico no es válida.") # print imprime que la dirección de correo no es válida.

print(" ") # print imprime un espacio