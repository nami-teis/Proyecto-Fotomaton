import pygame

class Boton:
    x: int
    y: int
    __width: int
    __height: int
    color_normal: tuple[int, int, int]
    color_hover: tuple[int, int, int]
    text: str
    text_color: tuple[int, int, int]
    font_size: int
    font: pygame.font.Font
    rect: pygame.Rect
    hovered: bool
    eliminado: bool
    presionado: bool
    __valor: int

    def __init__(self, x, y, width, height, color_normal, color_hover, text, text_color, font_size, valor=0):
        self.x = x
        self.y = y
        self.__width = width
        self.__height = height
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = pygame.Rect(x, y, width, height)
        self.hovered = False
        self.eliminado = False
        self.presionado = False
        self.__valor = valor

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int):
        if value >= 0:
            self.__width = value
        else:
            self.__width = 0

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int):
        if value >= 0:
            self.__height = value
        else:
            self.__height = 0

    @property
    def valor(self) -> int:
        return self.__valor

    @valor.setter
    def valor(self, value: int):
        self.__valor = value

    def draw(self, screen):
        if not self.eliminado: 
            if self.hovered: 
                color= self.color_hover
            else: 
                color = self.color_normal
            pygame.draw.rect(screen, color, self.rect)
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        if not self.eliminado: 
            self.hovered = self.rect.collidepoint(mouse_pos)

    def fue_presionado(self, mouse_pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Verificar si se hizo clic con el botón izquierdo del ratón
            if self.rect.collidepoint(mouse_pos):  # Verificar si las coordenadas del clic están dentro del área del botón
                self.presionado = True
                return True
        return False

    def eliminar(self): 
        self.eliminado = True

