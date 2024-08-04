# LA BIENVENIDA:
print("Bienvenido a tu calculadora IMC. Aqui podras ver tu nivel de masa corporal")
nombre = input("Ingresa tu nombre y apellido: \n")

#DATOS PARA LA CALCULADORA:

edad = int(input("Ingresa tu edad porfavor: \n"))
peso = float(input("Ingresa tu peso en Kg: \n"))
altura = float(input("Ingresa tu estatura en cm: \n"))
IMC = peso / altura**2 

#Ingresar los datos de IMC para ser calculados por cada persona

if IMC <= 18.5:
    print("Calificacion: Bajo Peso")
    print("Consume mas kilocalorias")
elif 18.5 <= IMC <= 29.9:
    print("Calificacion: Normal")
    print("Usted se ubica en su peso adecuado")
elif 25 <= IMC <= 29.9:
    print("Calificacion: Sobrepeso")
    print("Usted se ubica fuera de peso: Se recomienda realizar actividad fisica")
elif 30 <= IMC <= 34.9:
    print("Calificacion: Obesidad I")
    print("Cuidado! Debe realizar dieta baja en grasas y realizar actividad fisica")
elif 35 <= IMC <= 39.9:
    print("Calificacion: Obesidad II")
    print("¡Precaucion!: Su salud esta en riesgo, se recomienda moderada actividad fisica y dieta baja en kilocalorias")
elif IMC >= 40:
    print("Calificacion: Obesidad III")
    print("¡Alerta!: Su salud se encuentra en riesgo. Recomendacion de uso de Bypass")