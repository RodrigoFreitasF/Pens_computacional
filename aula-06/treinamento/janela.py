from random import random
import pygame
import time

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bem vindo ao Pygame")

# Loop principal do jogo
rodando = True
red = 0
green = 128
blue = 255
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # A tela ficará com fundo preto
    tela.fill((0, 0, 0))
    # Cria uma fonte
    fonte = pygame.font.SysFont("Arial", 36)
    texto = fonte.render("Olá, Pygame!", True, (red, green, blue))

    red += 1
    green += 1
    blue += 1
    if red > 255:
        red = 0
    if green > 255:
        green = 0
    if blue > 255:
        blue = 0



    #Calcula a posição central do texto
    texto_rect = texto.get_rect(center=(largura // 2, altura // 2))
    # Renderiza o texto na tela
    tela.blit(texto, texto_rect)

    # Atualiza a tela
    pygame.display.flip()


# Finaliza o Pygame
pygame.quit()
