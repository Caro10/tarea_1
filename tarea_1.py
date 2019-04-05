import math

PI = math.pi

ast = "*******"

Salida = ""
for index in range (1,7):
    Salida += ("%."+ str(index)+"s ") %ast
    Salida += ("%." + str(8-index) + "f ") %PI
print (Salida)

#Utilice su ejemplo como base y lo monté en un ciclo.