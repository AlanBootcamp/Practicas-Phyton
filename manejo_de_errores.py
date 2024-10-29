# numerador = 10
# denominador = 0
# cadena =  "3"
# numerico = 5

# print(numerador/denominador)
# print(cadena/numerico)

# try:
#     print(numerador/denominador)
# except (ZeroDivisionError, TypeError):
#  print("Ha ocurrido un error")
 
# try:
#     print(cadena/numerico)
# except TypeError:
#  print("Fin del programa")
# try:
#    print("Ha ocurrido un error de tipo")
# except:
#    print("Ha ocurrido un error desconocido")
# #ERROR 1 ZERODIVISIONERROR
#ERROR 2 TYPE ERROR


####################################
#Manejo de errores con excepciones y ciclos
try:

 dividendo = int (input("Ingresa el dividendo: "))
 divisor = int(input("Ingrese el divisor: "))
 print("El resultado es: ", dividendo/divisor)
except ValueError:
 print("Debes ingresar un numero")
except ZeroDivisionError:
 print("No se debe dividir entre cero")
 print("Fin del programa")