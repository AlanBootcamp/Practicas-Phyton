import requests

url= "https://pokeapi.co/api/v2/pokemon/pikachu"

try: 
    respuesta = requests.get (url, timeout=10)
except requests.Timeout:
    print("Error: El tiempo de espera ha sido finalizado")


if respuesta.status_code !=200 :
    print("Pokemon encontrado")
else:
    print(respuesta)

datos = respuesta.json()
nombre = datos ["name"]

print("movimientos de" + nombre + ":")

movimientos = datos ["moves"]
for i in range(int (len(movimientos))) :
    movimiento = movimientos [i] ["move"] ["name"]
    print(movimiento)