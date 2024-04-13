import pygame

class Label:
    x: int
    y: int
    text: str
    __font_size: int
    color: tuple[int, int, int]
    font: pygame.font.Font
    rendered_text: pygame.Surface
    rect: pygame.Rect
    eliminado: bool

    def __init__(self, x, y, text, font_size, color):
        self.x = x
        self.y = y
        self.text = text
        self.__font_size = font_size
        self.color = color
        self.font = pygame.font.Font(None, self.font_size)
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(topleft=(self.x, self.y))
        self.eliminado = False

    @property 
    def font_size(self): 
        return self.__font_size
    
    @font_size.setter
    def font_size(self, value): 
        if value < 0 : 
            self.__font_size = value
        else: 
            self.__font_size = 1

    def update(self, text):
        if not self.eliminado: 
            self.text = text
            self.rendered_text = self.font.render(self.text, True, self.color)
            self.rect = self.rendered_text.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        if not self.eliminado: 
            screen.blit(self.rendered_text, self.rect.topleft)
