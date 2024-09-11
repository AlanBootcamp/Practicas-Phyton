#Solicitar al usuario las cordenadas X & Y:

x = int (input("Ingrese coordenada X: "))
y= int(input("Ingrese la coordenada Y: "))

#Verficar que las coordenadas no sean 0:

if x == 0 or y == 0:
    print("Ninguna coordenada debe ser 0")

# Determinar que el cuadrante se encuentre en el punto

if x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I")
elif x < 0 and y > 0:
    print("EL punto se encuentra en el cuadrante II")
elif x < 0 and y <0:
    print("El punto se encuentra en el cuadrante III")
elif x > 0 and y < 0:
    print("El punto se encurntra en el cuadrante IV")