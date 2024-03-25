import cv2
import os
from os import remove
import time
from Camara import Camara

dimensiones = (2560, 1080)#ancho alto
cam = Camara(dimensiones)

ruta =  directorio_actual = os.path.dirname(os.path.abspath(__file__)) 

foto = False
while not foto:
    # Se comprueba que se obtiene imagen
    ret, frame = cam.leer()

    if ret == False:
        break

    cv2.imshow("imagen", frame)
    # Si se presiona la tecla de esc se guardará la foto
    if cv2.waitKey(1) == 27:
        nombre_archivo = os.path.join(ruta, 'foto.jpg')  # Construir la ruta completa con el nombre del archivo
        cv2.imwrite(nombre_archivo, frame)  # Guardamos imagen

        time.sleep(10)
        respuesta = input("¿Te gusta la imagen? s|n: ")
        if respuesta.lower() == "s":
            # se tendría que poner el comando de la impresora
            os.startfile(nombre_archivo, "print")
            foto = True
        else:
            remove(nombre_archivo)
cam.finalizar()
remove(nombre_archivo)