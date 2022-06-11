import pygame

class Paleta(pygame.Rect):
    pass

class Pong:
    _ANCHO = 800
    _ALTO = 420
    
    _MARGEN_LATERAL = (_ALTO/8)/2
    
    _ANCHO_PALETA = 12
    _ALTO_PALETA = _ALTO / 8

    _ALTO_RED = int(_ALTO/14)
    _ANCHO_RED = _ANCHO_PALETA/2
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))

        self.j1 = Paleta(self._MARGEN_LATERAL, (self._ALTO - self._ALTO_PALETA)/2, self._ANCHO_PALETA, self._ALTO_PALETA)
        self.j2 = Paleta(
        self._ANCHO-self._ANCHO_PALETA-self._MARGEN_LATERAL, #x
        (self._ALTO - self._ALTO_PALETA)/2, #y
        self._ANCHO_PALETA, #width
        self._ALTO_PALETA) #height
        self.crear_red()
        '''
        for y in range(int(self._ALTO_RED/2), self._ALTO, self._ALTO_RED*2):
            rectangulo = pygame.Rect(self._ANCHO/2-2, y, 4, self._ALTO_RED)
            pygame.draw.rect(self.pantalla, (255, 255, 255), rectangulo)
        '''
    def crear_red(self):
        for y in range(int(self._ALTO_RED/2), self._ALTO, self._ALTO_RED*2):
            rectangulo = pygame.Rect(self._ANCHO/2-2, y, self._ANCHO_RED, self._ALTO_RED)
            pygame.draw.rect(self.pantalla, (255, 255, 255), rectangulo)
        

    def bucle_principal(self):
        while True:
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j1)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j2)                   
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()
