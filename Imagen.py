import os
import cv2
from os import remove

class Imagen:

    directorio_guardado : str
    nombre : str 
    ruta : str

    def __init__(self, nombre):
        self.directorio_guardado = os.path.dirname(os.path.abspath(__file__)) 
        self.nombre = nombre

    def ruta_completa(self)->str: 
        return os.path.join(self.directorio_guardado, self.nombre)  # Construir la ruta completa con el nombre del archivo

    def mostrar(self, frame): 
        cv2.imshow("imagen", frame)
    
    def guardar(self, frame): 
        cv2.imwrite(self.ruta_completa(), frame)

    def borrar(self): 
        remove(self.ruta_completa())
