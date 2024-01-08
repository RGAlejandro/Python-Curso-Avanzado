import pygame
import random
import math
from pygame import mixer

#Inicializar Pygame
pygame.init()

#Crear la plantilla
pantalla = pygame.display.set_mode((800, 600))

#Titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("nave-espacial.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondoJuego.jpg")

#agregar musica
mixer.music.load("Y2meta.app - Hollow Knight OST - Dirtmouth (128 kbps).mp3")
mixer.music.play(-1)


#Jugador
img_jugador = pygame.image.load("icons8-nave-star-trek-kumari-64.png")
jugador_x = 332
jugador_y = 500
jugador_x_cambio = 0

#Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append( pygame.image.load("icons8-nave-romulana-star-trek-64.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.1)
    enemigo_y_cambio.append(50)

#Bala
img_bala = pygame.image.load("icons8-bala-50.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.5
bala_visible = False

#puntaje

puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10


#texto final de juego
fuente_final = pygame.font.Font("freesansbold.ttf", 40)
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x,y))

#funcion del enemigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

#funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16,y + 10))


# funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False

# funcion final del juego
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (100,200))

#Loop del juego
se_ejecuta = True

while se_ejecuta:

    # Fondo con formato RGB
    #pantalla.fill((85, 148, 255))

    #Fondo con imagen
    pantalla.blit(fondo, (0,0))

    for evento in pygame.event.get():

        #evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #evento presionar flechas
        if evento.type  == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)

        #evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #modificar ubicacion del jugador
    jugador_x += jugador_x_cambio

    #mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):

        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break


        enemigo_x[e] += enemigo_x_cambio[e]
    # mantener dentro de bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("Golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)
    #movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio



    jugador(jugador_x,jugador_y)

    mostrar_puntaje(texto_x,texto_y)


    #actuailzar
    pygame.display.update()

