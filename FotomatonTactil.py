from Boton import Boton
from Label import Label
from Imagen import Imagen
import subprocess
import pygame
import cv2
import numpy as np
from pygame import Surface
import os


class Fotomaton: 
    screen_width : int
    screen_height : int
    screen : Surface
    WHITE : tuple[int,int,int] = (255, 255, 255)
    BLACK: tuple[int,int,int]  = (0,0,0)
    BLUE : tuple[int,int,int] = (218,22,52)
    LIGHT_BLUE : tuple[int,int,int] = (208,26, 86)
    
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

    def __init__(self): 
        
        self.width = 800
        self.height = 600
        self.screen =  pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fotomatón teis")
    


    def imprimir(ruta_archivo, nombre_impresora=None):
        comando = ['lp']
        if nombre_impresora:
            comando.extend(['-d', nombre_impresora])
        comando.append(ruta_archivo)
        
        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate()
        
        if proceso.returncode == 0: #Para el momento de depuración, después debe eliminarse. Se puede dejar comentado por si aparece algún error durante la fase de producción (Remember clases patricia sjsjsjs)
            print("Archivo enviado a la impresora con éxito.")
        else:
            print(f"Error al imprimir el archivo: {error.decode()}")


    def cargar_imagenes(self): 
        directorio = os.getcwd()
        self.cortinaIzq = pygame.image.load(directorio + "\\Multimedia\\cortinas.png")
        self.cortinaDcha = pygame.image.load(directorio + "\\Multimedia\\cortinas.png")
        self.cortinaCentral = pygame.image.load(directorio + "\\Multimedia\\CortinaCentral.png")
        self.imagen_fondo =  pygame.image.load(directorio + "\\Multimedia\\fondo.jpg")

        #Escalamos las imágenes
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (self.width, self.height))
        self.cortinaIzq = pygame.transform.scale(self.cortinaIzq, (400, self.height))
        self.cortinaDcha = pygame.transform.scale(self.cortinaDcha, (400, self.height))
        self.cortinaCentral = pygame.transform.scale(self.cortinaCentral, (self.width + 100, 200))

    def posicionar_cortinas(self): 
        self.imagen_width, imagen_height = self.cortinaIzq.get_rect().size #Solo se hace una vez ya que son simétricas
        self.ci_x = 0
        self.ci_y = 0 
        self.cd_x = self.width - self.ci_x - self.imagen_width
        self.cd_y = 0

    def crear_botones(self): 
        width = 200 
        height = 50 
        color_normal = Fotomaton.BLUE
        color_hover = Fotomaton.LIGHT_BLUE
        color_texto = Fotomaton.WHITE
        self.font_size =  30
        
        centro_x = (self.width - width) // 2
        centro_y = (self.height - height) // 2
        self.boton_inicio =  Boton(centro_x, centro_y,  width, height, color_normal, color_hover, "Iniciar", color_texto, self.font_size)
        self.boton_capturar = Boton(centro_x, centro_y + 250, width, height, color_normal, color_hover, "Hacer foto", color_texto, self.font_size)
        self.boton_si = Boton( centro_x - 50, centro_y + 200, 100, 50, color_normal, color_hover, "Sí", color_texto, self.font_size)
        self.boton_no = Boton( centro_x + 150, centro_y + 200, 100, 50, color_normal, color_hover, "No", color_texto, self.font_size)

    def crear_textos(self): 
        x = (self.width - 175) // 2
        y = 125
        texto= "¿Te gusta la foto?"
        self.pregunta = Label(x,y,texto,self.font_size,Fotomaton.WHITE)

    def ejecutar(self, img : Imagen): 
        self.cargar_imagenes()
        self.posicionar_cortinas()
        self.crear_botones()
        self.crear_textos()

        cam = cv2.VideoCapture(0)

        temp_movimiento = 0 
        pasos = 15
        capturado = False 
        mostrar_boton_capturar = False
        mostrar_botones_si_no = False
        movimiento_cortinas = False
        capturar = False

        while not capturado : 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    capturado = True

                elif event.type == pygame.FINGERDOWN: 
                    touch_pos = (event.x, event.y) # Se actualiza cada vez que se detecta que se ha tocado la pantalla. 
                    if self.boton_inicio.fue_presionado(touch_pos, event): 
                        movimiento_cortinas = True
                        mostrar_boton_capturar = True

                    elif self.boton_capturar.fue_presionado(touch_pos, event):
                        img.guardar(frame)
                        mostrar_boton_capturar = False
                        mostrar_botones_si_no = True

                    elif self.boton_si.fue_presionado(touch_pos, event): 
                        self.imprimir(img.ruta)
                        img.borrar()
                        capturado = True

                    elif self.boton_no.fue_presionado(touch_pos, event): 
                        img.borrar()
                        mostrar_botones_si_no = False
                        mostrar_boton_capturar = True
                        capturar = True

            self.screen.blit(self.imagen_fondo, (0, 0))
            self.screen.blit(self.cortinaCentral, (-50, -50))

            if movimiento_cortinas: 
                self.boton_inicio.eliminar()
                
                if self.ci_x > -self.imagen_width - 500 and self.cd_x < self.width + 500:
                    if temp_movimiento < pasos:
                        temp_movimiento += 10
                    else:
                        self.ci_x -= 3
                        self.cd_x += 3
                        temp_movimiento = 0

                    
                    self.screen.blit(self.cortinaIzq, (self.ci_x, self.ci_y))
                    self.screen.blit(self.cortinaDcha, (self.cd_x, self.cd_y))
                    self.screen.blit(self.cortinaCentral, (-50, -50))
                    
                else : 
                    capturar = True
                    movimiento_cortinas = False

            else: 
                
                if not self.boton_inicio.eliminado: 
                    self.boton_inicio.update(touch_pos)
                else:  
                    self.boton_capturar.update(touch_pos)
                
                if mostrar_botones_si_no: 
                    self.boton_no.update(touch_pos)
                    self.boton_si.update(touch_pos)
            
                self.screen.blit(self.cortinaIzq, (self.ci_x, self.ci_y))
                self.screen.blit(self.cortinaDcha, (self.cd_x, self.cd_y))
                self.screen.blit(self.cortinaCentral, (-50, -50))
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
                    ret, frame = cam.read()
                    frame = np.rot90(frame) #Creo que es mejor imprimirla verticalmente para que se vea más grande. 
                    if ret:
                        pyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        # pyframe = np.rot90(pyframe) #En el caso de  no imprimirla verticalmente, se  eliminara la linea 238 y se descomentará esta
                        superficie_frame = pygame.surfarray.make_surface(pyframe)
                        superficie_frame = pygame.transform.scale(superficie_frame, (400, 300))

                        # Calcular las coordenadas para centrar la imagen en la pantalla
                        frame_x = (self.width - superficie_frame.get_width()) // 2
                        frame_y = (self.width - superficie_frame.get_height()-200) // 2

                        self.screen.blit(superficie_frame, (frame_x, frame_y))

            pygame.display.flip()

        pygame.quit()
        cam.release()

        if os.path.exists(img.ruta): 
            img.borrar()

        cv2.destroyAllWindows()
        