import cv2
import os
import time
from Camara import Camara
from Imagen import Imagen

class Fotomaton: 
    cam : Camara
    img : Imagen

    def __init__(self, dimensiones: tuple[int, int]):
        self.cam = Camara(dimensiones)
        self.img = Imagen("foto.jpg")

    def ejecutar(self): 
        foto = False
        while not foto:
            # Se comprueba que se obtiene imagen
            ret, frame = self.cam.leer()

            if ret == False:
                raise Exception ("No se ha podido obtener ninguna imagen de la camara")

            self.img.mostrar(frame)

            # Si se presiona la tecla de esc se guardará la foto, esto se deberá reemplazar con pygame
            if cv2.waitKey(1) == 27:
                self.img.guardar(frame)
                time.sleep(5)
                respuesta = input("¿Te gusta la imagen? s|n: ")
                if respuesta.lower() == "s":
                    # se tendría que poner el comando de la impresora
                    # os.startfile(nombre_archivo, "print") o hacer un script :/
                    foto = True
                else:
                    self.img.borrar()

        self.cam.finalizar()
        self.img.borrar()