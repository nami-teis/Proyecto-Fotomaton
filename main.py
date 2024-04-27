from Fotomaton import Fotomaton
from Imagen import Imagen
import pygame
import os


pygame.init()
f = Fotomaton()
img = Imagen("foto.jpg")

try : 
    f.ejecutar(img)
except: 
    if os.path.exists(img.ruta): 
        img.borrar()
