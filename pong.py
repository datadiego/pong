import pygame
ANCHO_PALETA = 10
ALTO_PALETA = 100
ANCHO = 800
ALTO = 400
MARGEN_LATERAL = (ALTO/6)/2
class Paleta(pygame.Rect):
    ARRIBA = True
    ABAJO = False

    def __init__(self, x, y):
        super(Paleta, self).__init__(x, y, ANCHO_PALETA, ALTO_PALETA)
        self.velocidad = 1
        #super(Paleta, self) equivale a Rect
        #.__init__(x, y, ANCHO_PALETA, ALTO_PALETA) llama al metodo init de Rect, coge los dos valores de posicion que entran al crear Paleta, y luego metemos las dos constantes globales que hemos creado al principio
    def mover(self, dir):
        if dir == self.ARRIBA:
            print("Muevete hacia arriba")
            self.y -= self.velocidad
            if self.y < 0:
                self.y = 0

        if dir == self.ABAJO:
            print("Muevete hacia abajo")
            self.y += self.velocidad
            if self.y > ALTO-ALTO_PALETA:
                self.y = ALTO - ALTO_PALETA
class Pong:
    
    
    _ANCHO_PALETA = 12
    _ALTO_PALETA = ALTO / 5

    _ALTO_RED = int(ALTO/12)
    _ANCHO_RED = _ANCHO_PALETA/2

    _CRT = True
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

        self.j1 = Paleta(MARGEN_LATERAL, (ALTO - ALTO_PALETA)/2)

        self.j2 = Paleta(ANCHO-ANCHO_PALETA-MARGEN_LATERAL, (ALTO - ALTO_PALETA)/2)

        self.crear_red()
        
    def crear_red(self):
        for y in range(int(self._ALTO_RED/2), ALTO, self._ALTO_RED*2):
            parte_red = pygame.Rect(ANCHO/2-2, y, self._ANCHO_RED, self._ALTO_RED)
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
            for y in range(1, ALTO, 2):
                pygame.draw.line(self.pantalla, (0,0,0), [0,y], [ANCHO, y])
        else:
            pass

    def bucle_principal(self):
        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        salir = True   
                if evento.type == pygame.QUIT:
                    salir = True
            estado_teclas = pygame.key.get_pressed()
            if estado_teclas[pygame.K_w]:
                self.j1.mover(Paleta.ARRIBA)
            if estado_teclas[pygame.K_s]:
                self.j1.mover(Paleta.ABAJO)
            if estado_teclas[pygame.K_UP]:
                self.j2.mover(Paleta.ARRIBA)
            if estado_teclas[pygame.K_DOWN]:
                self.j2.mover(Paleta.ABAJO)
            self.pantalla.fill((0,0,0))
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j1)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j2)
            self.display_seven_segment(200, 20, 5)
            self.display_seven_segment(ANCHO-200, 20, 6)
            self.CRT_filter()
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()