from Boton import Boton
from Label import Label
from Imagen import Imagen
from Camara import Camara
import pygame
import cv2
import numpy as np
from pygame import Surface
import os

# Inicialización de Pygame

class Fotomaton: 
    screen_width : int
    screen_height : int
    screen : Surface
    WHITE : tuple[int,int,int] = (255, 255, 255)
    BLACK: tuple[int,int,int]  = (0,0,0)
    RED : tuple[int,int,int] = (255, 0, 0)
    GREEN : tuple[int,int,int] = (0, 255, 0)
    
    cortinaIzq : Surface
    cortinaDcha :Surface
    imagen_fondo :Surface
    ci_x : int
    ci_y : int
    cd_x : int
    cd_y : int

    boton_inicio : Boton
    boton_capturar : Boton
    boton_si : Boton
    boton_no : Boton

    pregunta : Label


# Configuración de la pantalla

    def __init__(self): 
        
        self.width = 800
        self.height = 600
        self.screen =  pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fotomatón teis")
        

    def cargar_imagenes(self): 
        directorio = os.getcwd()
        self.cortinaIzq = pygame.image.load(directorio + "\\Multimedia\\CortinaIzq.png")
        self.cortinaDcha = pygame.image.load(directorio + "\\Multimedia\\CortinaDcha.png")
        self.imagen_fondo =  pygame.image.load(directorio + "\\Multimedia\\6715281.jpg")

        #Escalamos las imágenes
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (self.width, self.height))
        self.cortinaIzq = pygame.transform.scale(self.cortinaIzq, (200, self.height))
        self.cortinaDcha = pygame.transform.scale(self.cortinaDcha, (200, self.height))

    def posicionar_cortinas(self): 
        self.imagen_width, imagen_height = self.cortinaIzq.get_rect().size #Solo se hace una vez ya que son simétricas
        self.ci_x = 100
        self.ci_y = 0 
        self.cd_x = self.width - self.ci_x - self.imagen_width
        self.ci_y = 0

    def crear_botones(self): 
        width = 200 
        height = 50 
        color_normal = Fotomaton.GREEN
        color_hover = Fotomaton.RED
        color_texto = Fotomaton.WHITE
        self.font_size = 30
        
        centro_x = (self.width - width) // 2
        centro_y = (self.height - height) // 2
        self.boton_inicio =  Boton(centro_x, centro_y,  width, height, color_normal, color_hover, "Iniciar", color_texto, self.font_size)
        self.boton_capturar = Boton(centro_x, centro_y + 250, width, height, color_normal, color_hover, "Hacer foto", color_texto, self.font_size)
        self.boton_si = Boton( centro_x - 100, centro_y + 100, 100, 50, color_normal, color_hover, "Sí", color_texto, self.font_size)
        self.boton_no = Boton( centro_x + 100, centro_y + 100, 100, 50, color_normal, color_hover, "No", color_texto, self.font_size)

    def crear_textos(self): 
        x = 200
        y = 0
        texto= "¿Te gusta la foto?"
        self.pregunta = Label(x,y,texto,self.font_size,Fotomaton.WHITE)

    def ejecutar(self): 
        self.cargar_imagenes()
        self.posicionar_cortinas()
        self.crear_botones()
        self.crear_textos()

        cam = Camara(0)
        img = Imagen("foto.jpg")

        capturado = False 
        mostrar_boton_capturar = False
        mostrar_botones_si_no = False
        movimiento_cortinas = True
        pasos = 15
        temp_movimiento = 0
        capturar = False

        while not capturado : 
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    capturado = True
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if self.boton_inicio.fue_presionado(mouse, event): 
                        movimiento_cortinas = True
                        mostrar_boton_capturar = True
                    elif self.boton_capturar.fue_presionado(mouse, event):
                        img.guardar(frame)
                        mostrar_boton_capturar = False
                        mostrar_botones_si_no = True
                    elif self.boton_si.fue_presionado(mouse, event): 
                        #imprimir la fotoo
                        img.borrar()
                        capturado = True
                    elif self.boton_no.fue_presionado(mouse, event): 
                        img.borrar()
                        mostrar_botones_si_no = False
                        mostrarCapturar = True

            if movimiento_cortinas: 
                self.boton_inicio.eliminar()
                if self.ci_x > 0 or self.cd_x < self.width - self.imagen_width: 
                    if temp_movimiento < pasos: 
                        temp_movimiento = 10 
                    else: 
                        self.ci_x = max(0, self.ci_x - 1)
                        self.cd_x = min(self.width - self.imagen_width, self.cd_x + 1)
                        temp_movimiento = 0 
                else : 
                    capturar = True

            if not self.boton_inicio.eliminado: 
                self.boton_inicio.update(mouse)
            else:  
                self.boton_capturar.update(mouse)
            
            if mostrar_botones_si_no: 
                self.boton_no.update(mouse)
                self.boton_si.update(mouse)
            
            self.screen.blit(self.imagen_fondo, (0,0))
            self.screen.blit(self.cortinaIzq, (self.ci_x, self.ci_y))
            self.screen.blit(self.cortinaDcha, (self.cd_x, self.cd_y))
            self.boton_inicio.draw(self.screen)
        
            if mostrar_boton_capturar: 
                self.boton_capturar.draw(self.screen)
            
            if mostrar_botones_si_no: 
                capturar = False
                self.pregunta.draw(self.screen)
                self.boton_si.draw(self.screen)
                self.boton_no.draw(self.screen)
                self.screen.blit(superficie_frame, (frame_x, frame_y))

            if capturar: 
                ret, frame = cam.leer()
                if ret:
                    pyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    pyframe = np.rot90(pyframe)
                    superficie_frame = pygame.surfarray.make_surface(pyframe)
                    superficie_frame = pygame.transform.scale(superficie_frame, (300, 200))

                    # Calcular las coordenadas para centrar la imagen en la pantalla
                    frame_x = (self.width - superficie_frame.get_width()) // 2
                    frame_y = (self.width - superficie_frame.get_height()) // 2

                    self.screen.blit(superficie_frame, (frame_x, frame_y))

            pygame.display.flip()

        pygame.quit()
        cam.finalizar()
        cv2.destroyAllWindows()
        

