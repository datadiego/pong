import pygame
    
class Paleta(pygame.Rect):
    pass   

class Pong:
    _ANCHO = 800
    _ALTO = 400
    
    _MARGEN_LATERAL = (_ALTO/6)/2
    
    _ANCHO_PALETA = 12
    _ALTO_PALETA = _ALTO / 5

    _ALTO_RED = int(_ALTO/12)
    _ANCHO_RED = _ANCHO_PALETA/2

    _CRT = True
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))

        self.j1 = Paleta(self._MARGEN_LATERAL, (self._ALTO - self._ALTO_PALETA)/2, self._ANCHO_PALETA, self._ALTO_PALETA)

        #Partes de un 7 segmentos
        '''
        self.a = pygame.Rect(200, self._MARGEN_LATERAL, 50, 8)                  
        self.b = pygame.Rect(200, self._MARGEN_LATERAL+50, 50, 8)
        self.c = pygame.Rect(200, self._MARGEN_LATERAL+100, 50, 8)
        self.d = pygame.Rect(200, self._MARGEN_LATERAL, 8, 50)
        self.e = pygame.Rect(250-self._ALTO_SEGMENTO, self._MARGEN_LATERAL, 8, 50)
        '''

        self.j2 = Paleta(
        self._ANCHO-self._ANCHO_PALETA-self._MARGEN_LATERAL, #x
        (self._ALTO - self._ALTO_PALETA)/2, #y
        self._ANCHO_PALETA, #width
        self._ALTO_PALETA) #height

        self.crear_red()
        
    def crear_red(self):
        for y in range(int(self._ALTO_RED/2), self._ALTO, self._ALTO_RED*2):
            parte_red = pygame.Rect(self._ANCHO/2-2, y, self._ANCHO_RED, self._ALTO_RED)
            pygame.draw.rect(self.pantalla, (255, 255, 255), parte_red)
        
    def display_seven_segment(self, posx, posy, val):
        valores_segmentos = {0:"abcdef", 1:"bc", 2:"abged", 3:"abgcd", 4:"fgbc", 5:"afgcd", 6:"afgedc", 7: "abc", 8:"abcdefg", 9:"abcdfg"}
        codificado = valores_segmentos[val]
        HOR_WIDTH = 25
        HOR_HEIGHT = 10

        VER_WIDTH = HOR_HEIGHT
        VER_HEIGHT = HOR_WIDTH
        for segmento in codificado:
            if segmento == "a":
                self.a = pygame.Rect(posx, posy, HOR_WIDTH, HOR_HEIGHT)
                pygame.draw.rect(self.pantalla, (255, 255, 255), self.a)
            if segmento == "b":
                self.b = pygame.Rect(posx+HOR_WIDTH-HOR_HEIGHT, posy, VER_WIDTH, VER_HEIGHT)
                pygame.draw.rect(self.pantalla, (255, 255, 255), self.b)
            if segmento == "c":
                self.c = pygame.Rect(posx+HOR_WIDTH-HOR_HEIGHT, posy+VER_HEIGHT, VER_WIDTH, VER_HEIGHT)
                pygame.draw.rect(self.pantalla, (255, 255, 255), self.c)
            if segmento == "d":
                self.d = pygame.Rect(posx, posy+VER_HEIGHT*2-VER_WIDTH, HOR_WIDTH, HOR_HEIGHT)
                pygame.draw.rect(self.pantalla, (255, 255, 255), self.d)
            if segmento == "e":
                self.e = pygame.Rect(posx, posy+VER_HEIGHT, VER_WIDTH, VER_HEIGHT)
                pygame.draw.rect(self.pantalla, (255, 255, 255), self.e)
            if segmento == "f":
                self.f = pygame.Rect(posx, posy, VER_WIDTH, VER_HEIGHT)
                pygame.draw.rect(self.pantalla, (255, 255, 255), self.f)
            if segmento == "g":
                self.g = pygame.Rect(posx, posy+VER_HEIGHT-(VER_WIDTH/2), HOR_WIDTH, HOR_HEIGHT)
                pygame.draw.rect(self.pantalla, (255, 255, 255), self.g)
    def CRT_filter(self):
        if self._CRT:
            for y in range(0, self._ALTO, 2):
                pygame.draw.line(self.pantalla, (0,0,0), [0,y], [self._ANCHO, y])
        else:
            pass

    def bucle_principal(self):
        while True:
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j1)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j2)
            self.display_seven_segment(200, 20, 5)
            self.display_seven_segment(self._ANCHO-200, 20, 6)
            self.CRT_filter()
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()