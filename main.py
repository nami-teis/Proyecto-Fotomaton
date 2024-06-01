from FotomatonTactil import Fotomaton
from Imagen import Imagen
import pygame
import os


pygame.init()
f = Fotomaton()
img = Imagen("foto.jpg")

try : 
    f.ejecutar(img)
except:  # De esta forma nos aseguramos que en caso de que el programa rompa, no se quede guardada ninguna foto
    if os.path.exists(img.ruta): 
        img.borrar()
