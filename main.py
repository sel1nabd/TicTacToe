
# SETTING UP THE SCREEN

import pygame

pygame.init()

GameScreen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")

background_colour = (255, 255, 255) # white
line_colour = (0, 0, 0) # black

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    GameScreen.fill(background_colour)

    pygame.draw.line(GameScreen, line_colour, (200, 0), (200, 600), 5)  # from top to bottom
    pygame.draw.line(GameScreen, line_colour, (400, 0), (400, 600), 5)  # from top to bottom

    # 3) Draw horizontal lines
    pygame.draw.line(GameScreen, line_colour, (0, 200), (600, 200), 5)  # from left to right
    pygame.draw.line(GameScreen, line_colour, (0, 400), (600, 400), 5)  # from left to right

    pygame.display.update()

pygame.quit()


