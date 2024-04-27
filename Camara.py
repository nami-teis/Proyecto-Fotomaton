import cv2
import os

class Camara: 
    # cam : VideoCapture 

    def __init__(self,num : int):
        #abrir la cámara: 
        self.cam = cv2.VideoCapture(num)


    def leer(self): 
        ret, frame = self.cam.read()
        return ret, frame
    
    def finalizar(self): 
        self.cam.release()  