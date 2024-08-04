#Agregar los datos de usuario

print("Bienvenido a su calculadora IMC, por favor irgrese sus datos:")
nombre = input ("Ingrese su nombre: ")
apellido =input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

if(edad < 18):
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")

altura = float(input("Ingrese su estatura en cm: "))
masa = float(input("Ingrese su peso en kg: "))

#Calcula la masa IMC

IMC = masa / altura**2

#Confirmacion de mayor o menor de edad

