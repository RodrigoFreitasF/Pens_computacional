import pygame
import random
import time
# Constantes (normalmente escrevemos tudo em maiúsculo em Python)
LARGURA = 1920
ALTURA = 1100
PRETO = (0, 0, 0)

# Inicializa o Pygame
pygame.init()

# Define as dimensões e título da janela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("descanso de tela")


def tela_inicial():
    # Preenche a tela de preto
    tela.fill(PRETO)
    pygame.display.flip()


# Loop principal do jogo
tela_inicial()
rodando = True
num_circulos = 1500
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    if num_circulos <= 0:
        num_circulos = random.randint(1000, 4500)
        time.sleep(2)
        tela_inicial()
    cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pos = (random.randint(0, LARGURA), random.randint(0, ALTURA))
    raio = random.randint(2, 40)
    pygame.draw.circle(tela, cor, pos, raio)
    #time.sleep(0.01)
    pygame.display.flip()
    num_circulos -= 1
# Finaliza o Pygame
pygame.quit()
