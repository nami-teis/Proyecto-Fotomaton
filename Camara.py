import cv2
import os

class Camara: 
    # cam : VideoCapture 

    def __init__(self, dimensiones : tuple[int,int]):
        #abrir la cámara: 
        self.cam = cv2.VideoCapture(0)
        #Establecer dimensiones de la imagen que se va a capturar: 
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, dimensiones[0])
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dimensiones[1])

    def leer(self): 
        ret, frame = self.cam.read()
        return ret, frame
    
    def finalizar(self): 
        self.cam.release()  