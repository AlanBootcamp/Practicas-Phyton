import requests
import json
import os
from PIL import Image
from io import BytesIO

## BIENVENIDA A LA POKEDEX

print("Bienvenido a tu POKEDEX")

## OBTENCION DE DATOS DEL POKEMON
def pokemon(nombre):
 url= f"https://pokeapi.co/api/v2/pokemon/" + pokemon
 respuesta = requests.get(url)

##VERIFICACION SI LA OPERACION ES EXITOSA.
 if respuesta.status_code == 404:
    print("Error! El Pokemon no ha sido encontrado")
 elif respuesta.status_code != 200: 
  print("Oh no! Hubo un problema de conexion")

## DATOS POKEMON
 datos= respuesta.json()
 data_pokemon = {
        "nombre": datos ["name"],
        "peso" : datos["weight"],
        "tamaño": datos["height"],
        "movimientos": [movimiento["move"]["name"] for movimiento in datos["moves"]],
        "habilidades": [habilidad["ability"]["name"] for habilidad in datos["abilities"]],
        "tipos": [tipo["type"]["name"] for tipo in datos["types"]],
        "Imagen": datos ['sprites'] ['front_default']
        }
    ##IMAGENES Y ESTADISTICAS DEL POKÉMON
 print(f"\nNombre{data_pokemon["nombre"].capitalize()}")
 print(f"peso{data_pokemon['peso']}")
 print(f"tamaño{data_pokemon['tamaño']}")
 print(f"Habilidades: {', '.join(data_pokemon['habilidades'][:2])}...")
 print(f"Tipos: {', '.join(data_pokemon['tipos'])}")
    
     ## DESCARGA Y MUESTRA DE IMAGEN POKÉMON
 if data_pokemon["Imagen"]:
        imagen_response = requests.get(data_pokemon["Imagen"])
        imagen = Image.open(BytesIO(imagen_response.content))
        imagen.show

        ##FUNCION PARA GUARDAR DATOS EN CARPETAS A NOMBRE POKEDEX
        def guardar_json (Pokemon , nombre_archivo = "Pokedex/Pokemon.json"):
            if not os.path.exists ("Pokedex/Pokemon.json"):
                os.makedirs("Pokedex/Pokemon.json")
                with open (nombre_archivo , "w") as archivo:
                    json.dump(pokemon , archivo , indent= 4)
                    print(f"\nDatos de {pokemon['nombre'].capitalize()} guardados en '{nombre_archivo}'.")
             ## DATA PRINCIPAL
        def main():
         nombre_pokemon = input("Ingresa el nombre del Pokemon: ")
         pokemon (nombre_pokemon)

         if pokemon: 
            guardar_json (pokemon , f"pokedex/{nombre_pokemon()}.json")  
        main()