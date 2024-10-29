# # f_archivo = open("archivo1.txt", "w") # w= Write (escribir) escribir o sobreescribir un archivo 
# # print(f_archivo)
# # f_archivo.write("HOLA MUNDO")
# # f_archivo.close()

# f_archivo = open("archivo1.txt", "w")
# f_archivo.write ("Este es mi primer archivo")
# f_archivo.close()

# f_lectura = open("archivo1.txt" , "r") # r = read (leer) leer el archivo
# print(f_lectura.read())
# f_lectura.close()

# print(f_archivo)
# print(f_lectura)


################################################################
#SENTENCIAS WHIT Y AS

# f_lectura = open("archivo1.txt", "r")
# print(f_lectura.closed)
# f_lectura.close()
# print(f_lectura.closed)

# with open("archivo1.txt", "r") as f_lectura:
#     print(f_lectura.closed)
# print(f_lectura.closed)

# with open("archivo1.txt", "a") as f_archivo: #a = append (agregar) agregar al final del archivo
#     f_archivo.write("\nEste es mi pirmer archivo 2")
#     f_archivo.write("Este es mi primer archivo 3")
#     f_archivo.write("\n")
#     f_archivo.write("\tEste es mi primer archivo 4")
# with open("archivo1.txt", "r") as f_lectura:
#   contenido = f_lectura.read()
#   print(f'***{contenido}***')
#   contenido = f_lectura.read()
#   print(f'***{contenido}***')



##########################################################3
# Lectura de archivo linea a linea

# with open('archivo1.txt', 'r') as f_lectura:
#     numero_de_lineas = 0
#     for i in f_lectura:
#         numero_de_lineas +=1
#         print(f'linea{numero_de_lineas}: {i}')
#         print(f'El archivo tiene {numero_de_lineas} lineas')

# Creando una lista a partir de un archivo 

with open ('archivo1.txt', 'r') as f_archivo:
    lista_archivo = f_archivo.readlines()
    print(lista_archivo)

print(lista_archivo)

lista_archivo[1] = "Este es mi primer archivo 2\n"
lista_archivo.insert (2, "Este es mi primer archivo 3 \n")
print (lista_archivo)

with open("archivo1.txt", "w") as f_archivo:
    f_archivo.writelines(lista_archivo)