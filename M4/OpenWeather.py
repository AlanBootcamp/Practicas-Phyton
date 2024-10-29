import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

pokemon =input ("Ingresa un Pokemon: ")

url = "https://pokeapi.co/api/v2/pokemon/"  + pokemon
respuesta = requests.get(url)

if respuesta.status_code !=200 :
    print("Pokemon no encontrado")
    exit ()

datos = respuesta.json()

try: 
    url_image = datos ["sprites"] ["front_default"]
    image = Image.open(urlopen(url_image))
except :
    print("El Pokemon no tiene imagen")
    exit() 

plt.title(datos["name"])
imgplot = plt.imshow(image)
plt.show