from random import randint
import pygame
ANCHO_PALETA = 10
ALTO_PALETA = 100
SIZE_BALL = 15
ANCHO = 800
ALTO = 400
MARGEN_LATERAL = (ALTO/6)/2
PUNTOS_J1 = 0
PUNTOS_J2 = 0
class Paleta(pygame.Rect):
    ARRIBA = True
    ABAJO = False

    def __init__(self, x, y):
        super(Paleta, self).__init__(x, y, ANCHO_PALETA, ALTO_PALETA)
        self.velocidad = 5
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

class Pelota(pygame.Rect):
    def __init__(self):
        super(Pelota, self).__init__((ANCHO-SIZE_BALL)/2+1, (ALTO-SIZE_BALL)/2, SIZE_BALL, SIZE_BALL)
        self.velocidad_x = randint(-5, 5)
        self.velocidad_y = randint(-5, 5)
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-5,5)
        while self.velocidad_y == 0:
            self.velocidad_y = randint(-5,5)
        self.PUNTOS_J1 = 0
        self.PUNTOS_J2 = 0
    def mover(self):
        self.y += self.velocidad_y
        self.x += self.velocidad_x
        if self.x > ANCHO:
            self.x = ANCHO/2
            self.y = ALTO/2
            self.velocidad_x *= -1
            self.PUNTOS_J1 += 1
        if self.x < 0:
            self.x = ANCHO/2
            self.y = ALTO/2
            self.velocidad_x *= -1
            self.PUNTOS_J2 += 1
        if self.y < 0:
            self.velocidad_y *= -1
        if self.y > ALTO-SIZE_BALL:
            self.velocidad_y *= -1
            

class Pong:
    _ANCHO_PALETA = 12
    _ALTO_PALETA = ALTO / 5

    _ALTO_RED = int(ALTO/12)
    _ANCHO_RED = _ANCHO_PALETA/2

    _CRT = False

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.clock = pygame.time.Clock()
        self.j1 = Paleta(MARGEN_LATERAL, (ALTO - ALTO_PALETA)/2)
        self.j2 = Paleta(ANCHO-ANCHO_PALETA-MARGEN_LATERAL, (ALTO - ALTO_PALETA)/2)
        self.ball = Pelota()
        
        
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
                pygame.draw.line(self.pantalla, (0,0,0, 200), [0,y], [ANCHO, y])
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
            self.crear_red()
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j1)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.j2)
            self.display_seven_segment(200, 20, self.ball.PUNTOS_J1)
            self.display_seven_segment(ANCHO-200, 20, self.ball.PUNTOS_J2)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.ball)
            self.ball.mover()
            self.CRT_filter()
            
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()