import pygame
import sys


def main(x, y, color):
    pygame.init()
    Pantalla = pygame.display.set_mode((x, y))
    Titulo = pygame.display.set_caption("Dia X")
    Pantalla.fill(color)
    drawsquare_red(Pantalla)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
    
def drawsquare_red(pantalla):
    color2 = rojo
    pos_x = int(input("en que posicion de x quieres que este?: "))
    pos_y = int(input("en que posicion de y quieres que este?: "))
    oc_x = int(input("cuantas posiciones en x quieres quen ocupe?: "))
    oc_y = int(input("cuantas posiciones en y quieres que ocupe?: "))
    pygame.draw.rect(pantalla, color2, (pos_x, pos_y, oc_x, oc_y))

def drawsquare_blue(pantalla):
    color2 = azul
    pos_x = int(input("en que posicion de x quieres que este?: "))
    pos_y = int(input("en que posicion de y quieres que este?: "))
    oc_x = int(input("cuantas posiciones en x quieres quen ocupe?: "))
    oc_y = int(input("cuantas posiciones en y quieres que ocupe?: "))
    pygame.draw.rect(pantalla, color2, (pos_x, pos_y, oc_x, oc_y))

def drawsquare_green(pantalla):
    color2 = verde
    pos_x = int(input("en que posicion de x quieres que este?: "))
    pos_y = int(input("en que posicion de y quieres que este?: "))
    oc_x = int(input("cuantas posiciones en x quieres quen ocupe?: "))
    oc_y = int(input("cuantas posiciones en y quieres que ocupe?: "))
    pygame.draw.rect(pantalla, color2, (pos_x, pos_y, oc_x, oc_y))

def drawsquare_black(pantalla):
    color2 = negro
    pos_x = int(input("en que posicion de x quieres que este?: "))
    pos_y = int(input("en que posicion de y quieres que este?: "))
    oc_x = int(input("cuantas posiciones en x quieres quen ocupe?: "))
    oc_y = int(input("cuantas posiciones en y quieres que ocupe?: "))
    pygame.draw.rect(pantalla, color2, (pos_x, pos_y, oc_x, oc_y))

def drawsquare_white(pantalla):
    color2 = blanco
    pos_x = int(input("en que posicion de x quieres que este?: "))
    pos_y = int(input("en que posicion de y quieres que este?: "))
    oc_x = int(input("cuantas posiciones en x quieres quen ocupe?: "))
    oc_y = int(input("cuantas posiciones en y quieres que ocupe?: "))
    pygame.draw.rect(pantalla, color2, (pos_x, pos_y, oc_x, oc_y))


if __name__ == "__main__":
    blanco = (255, 255, 255)
    negro = (0, 0, 0)
    rojo = (255, 0, 0)
    verde = (0, 255, 0)
    azul = (0, 0, 255)
    main(400, 500, azul)