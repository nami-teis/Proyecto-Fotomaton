import cv2
import os
from os import remove
import time

#abrir la cámara:
cam = cv2.VideoCapture(0)

#Establecer dimensiones de la imagen que se va a capturar: 
dimensiones = (2560, 1080)#ancho alto
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dimensiones[0])
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dimensiones[1])

ruta = "C:\\Users\\nadia\\Desktop\\imagen.jpg" #Obviamente hay que cambiarlo con el path 

foto = False
while not foto:    
    #Se comprueba que se obtiene imagen
    ret, frame = cam.read()

    if ret == False: 
        break

    cv2.imshow("imagen", frame)
    #Si se presiona la tecla de esc se guardará la foto 
    if cv2.waitKey(1) == 27: 
             
        img = cv2.imwrite(ruta, frame) #Guardamos imagen

        cv2.imshow("Hola", img)
        time.sleep(10)
        respuesta = input("¿Te gusta la imagen? s|n: ")
        if respuesta.lower() == "s":
            #se tendría que poner el comando de la impresora 
            os.startfile(ruta, "print")
            foto = True
        else: 
            remove(ruta)
cam.release()  #Finalizamos la cámara 