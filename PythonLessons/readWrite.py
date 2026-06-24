#Leyendo un archivo txt, esta vez es test.txt y esta en el mismo directorio.

file = open("test.txt")
#1 - Read all the content of file - Este lee todo el documento

print(file.read())

#2 - Tambien puedes leer caracteres poniendo los caracteres en el parentesis :
#print(file.read(2))

#3 - Leyendo una sola linea a la vez, este ejemplo lee las tres primeras lineas:
# print(file.readline())
# print(file.readline())
# print(file.readline())

#4 Imprimiendo line usando readline method

# line = file.readline()
#
# while line != "":
#     print(line)
#     line = file.readline()

# #5 Sacando todos los valores del txt con for, puede servir para crear listas.
# for line in file.readlines():
#     print(line)

file.close()