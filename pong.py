import pygame

class Paleta(pygame.Rect):
    pass

class Pong:

    _ALTO = 200
    _ANCHO = 800
    _MARGEN_LATERAL = (_ALTO/10)/2
    
    _ALTO_RED = int(_ALTO/15)
    _ANCHO_PALETA = 12
    _ALTO_PALETA = _ALTO / 5
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))

        self.j1 = Paleta(self._MARGEN_LATERAL, (self._ALTO - self._ALTO_PALETA)/2, self._ANCHO_PALETA, self._ALTO_PALETA)
        self.j2 = Paleta(
        self._ANCHO-self._ANCHO_PALETA-self._MARGEN_LATERAL, #x
        (self._ALTO - self._ALTO_PALETA)/2, #y
        self._ANCHO_PALETA, #width
        self._ALTO_PALETA) #height
        '''
        for y in range(int(self._ALTO_RED/2), self._ALTO, self._ALTO_RED*2):
            rectangulo = pygame.Rect(self._ANCHO/2-2, y, 4, self._ALTO_RED)
            pygame.draw.rect(self.pantalla, (255, 255, 255), rectangulo)
        '''
    def crear_red(self, alto_segmento):
        for y in range(int(alto_segmento/2), self._ALTO, alto_segmento*2):
            rectangulo = pygame.Rect(self._ANCHO/2-2, y, self._ANCHO_PALETA, alto_segmento)
            pygame.draw.rect(self.pantalla, (255, 255, 255), rectangulo)
        

    def bucle_principal(self):
        
        while True:
            
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j1)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j2)                   
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.crear_red(25)
    juego.bucle_principal()
