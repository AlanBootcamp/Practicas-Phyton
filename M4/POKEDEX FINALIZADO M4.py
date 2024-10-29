import requests
import json
import os
from PIL import Image
from io import BytesIO

# Función para obtener datos de un Pokémon
def obtener_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)
    
    if response.status_code == 404:
        print(f"El Pokémon '{nombre}' no existe. Intenta con otro nombre.")
        return None
    elif response.status_code != 200:
        print("Hubo un problema al conectar con la API.")
        return None

    # Parsear los datos del Pokémon
    datos = response.json()
    informacion_pokemon = {
        "nombre": datos["name"],
        "peso": datos["weight"],
        "altura": datos["height"],
        "tipos": [tipo["type"]["name"] for tipo in datos["types"]],
        "habilidades": [habilidad["ability"]["name"] for habilidad in datos["abilities"]],
        "movimientos": [movimiento["move"]["name"] for movimiento in datos["moves"]],
        "imagen": datos["sprites"]["front_default"]
    }

    # Mostrar imagen y estadísticas básicas
    print(f"\nNombre: {informacion_pokemon['nombre'].capitalize()}")
    print(f"Peso: {informacion_pokemon['peso']}")
    print(f"Altura: {informacion_pokemon['altura']}")
    print(f"Tipos: {', '.join(informacion_pokemon['tipos'])}")
    print(f"Habilidades: {', '.join(informacion_pokemon['habilidades'][:5])}...")  # Solo las primeras 5 habilidades

    # Descargar y mostrar la imagen
    if informacion_pokemon["imagen"]:
        imagen_response = requests.get(informacion_pokemon["imagen"])
        imagen = Image.open(BytesIO(imagen_response.content))
        imagen.show()

    return informacion_pokemon

# Función para guardar datos en un archivo JSON
def guardar_en_json(pokemon, nombre_archivo="pokedex/pokemon.json"):
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")
    
    with open(nombre_archivo, "w") as archivo:
        json.dump(pokemon, archivo, indent=4)
    print(f"\nDatos de {pokemon['nombre'].capitalize()} guardados en '{nombre_archivo}'.")

# Función principal
def main():
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")
    pokemon = obtener_pokemon(nombre_pokemon)
    
    if pokemon:
        guardar_en_json(pokemon, f"pokedex/{nombre_pokemon.lower()}.json")

main()