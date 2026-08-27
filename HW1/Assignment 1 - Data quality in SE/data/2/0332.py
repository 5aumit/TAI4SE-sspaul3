"""
Escreva um programa que leia as coordenadas x e y de um ponto R² e calcule
sua distância da origem(0,0).
"""
import math

print("Origem = 0")

x = int(input("X: "))
y = int(input("Y: "))

aux = (x*x)+(y*y)
dist = math.sqrt(aux)


print("Distância da origem {:.2f}".format(dist))