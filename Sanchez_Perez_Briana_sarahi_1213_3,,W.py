print(" ")# print imprime un espacio

print("Sanchez Perez Briana Sarahi_1213_3W") 
print(" ")  # print imprime un espacio

def my_function(punto1, punto2): # definiendo funcion
    dx = punto2[0] - punto1[0]  # Diferencia en x
    dy = punto2[1] - punto1[1]  # Diferencia en y
    return (dx, dy)  # Retorna la distancia dirigida como un tuple

x1 = float(input("Introduce la coordenada x del primer punto: ")) # pide coordenada x del primer punto
y1 = float(input("Introduce la coordenada y del primer punto: ")) # pide coordenada y del primer punto
x2 = float(input("Introduce la coordenada x del segundo punto: ")) # pide coordenada x del segundo punto 
y2 = float(input("Introduce la coordenada y del segundo punto: ")) # pide coordenada y del segundo punto

punto1 = (x1, y1) # crea una tupla
punto2 = (x2, y2) # crea una tupla

distancia = my_function(punto1, punto2) # calcula a distancia
print("La distancia dirigida entre los puntos es:", distancia) # print imprime la distacia entre los puntos

print(" ")  # print imprime un espacio