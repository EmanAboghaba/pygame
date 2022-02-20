import sys
import pygame
import numpy as np


pygame.init()

WIDTH = 600
HEIGHT = WIDTH
line_width = 15
BG_COLOR = (38, 50, 56)
line_color = (96, 125, 139)
b_row = 3
b_col = 3
space = WIDTH//b_row
circle_color = (240, 128, 128)
x_color = (255,228,225)
x_space = 55
circle_r = 60
circle_w = 20
cross_w = 50
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(BG_COLOR)
pygame.display.set_caption("Tic Tac Toe Game!!")
screen = np.zeros((b_row, b_col))


def draw_lines():
    pygame.draw.line(WIN, line_color, (0, space), (WIDTH, space), line_width)
    pygame.draw.line(WIN, line_color, (0, 2*space), (WIDTH, 2*space), line_width)

    pygame.draw.line(WIN, line_color, (space, 0), (space, HEIGHT), line_width)
    pygame.draw.line(WIN, line_color, (2*space, 0), (2*space, HEIGHT), line_width)


draw_lines()


def mark_screen(row, col, player):
    screen[row][col] = player


def empty_screen(row, col):
    return screen[row][col] == 0


def is_full():
    for row in range(b_row):
        for col in range(b_col):
            if screen[row][col] == 0:
                return False
    return True


def win_line(player):

    for col in range(b_col):
        if screen[0][col] == player and screen[1][col] == player and screen[2][col] == player:
            win_col(col, player)
            return True

    for row in range(b_row):
        if screen[row][0] == player and screen[row][1] == player and screen[row][2] == player:
            win_row(row, player)
            return True
    if screen[0][0] == player and screen[1][1] == player and screen[2][2] == player:
        win_diagonal1(player)
        return True
    if screen[2][0] == player and screen[1][1] == player and screen[0][2] == player:
        win_diagonal2(player)
        return True

    return False



def win_col(col,player):
    x1 = col*space + space//2
    if player == 1:
       color = circle_color
    elif player == 2:
       color = x_color
    pygame.draw.line(WIN,color, (x1, 16), (x1, HEIGHT-16), 16)


def win_row(row,player):
    r1 = row * space + space//2
    if player == 1:
        color1 = circle_color
    elif player == 2:
        color1 = x_color
    pygame.draw.line(WIN, color1, (16, r1), (WIDTH - 16, r1), 16)


def win_diagonal1(player):

    if player == 1:
        color2 = circle_color
    elif player == 2:
        color2 = x_color
    pygame.draw.line(WIN, color2, (16, 16), (WIDTH - 16, HEIGHT-16), 16)

def win_diagonal2(player):
    if player == 1:
        color3 = circle_color
    elif player == 2:
        color3 = x_color
    pygame.draw.line(WIN, color3, (16, HEIGHT-16), (WIDTH - 16, 16), 16)


def draw_shape():
    for row in range(b_row):
        for col in range(b_col):
            if screen[row][col] == 1:
                pygame.draw.circle(WIN, circle_color, (int(col*space+100), int(row*space+100)), circle_r, circle_w)
            if screen[row][col] == 2:
                pygame.draw.line(WIN, x_color, (col * space + x_space, row * space + space - x_space), (col * space + space - x_space, row * space + x_space), cross_w)
                pygame.draw.line(WIN, x_color, (col * space + x_space, row * space + x_space),
                                 (col * space + space - x_space, row * space + space - x_space), cross_w)


def draw_winner(player):
    font = pygame.font.SysFont(None, 40)
    winner = "player " + str(player) + " wins !!"
    win_color = font.render(winner, True, "red")
    pygame.draw.rect(WIN, "black", (WIDTH//2 - 80, HEIGHT//2 - 90, 200, 60))
    WIN.blit(win_color, (WIDTH//2 - 80, HEIGHT//2 - 90))


player = 1
c=0
end_game = False
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not end_game:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY // space)
            clicked_col = int(mouseX // space)
            if empty_screen(clicked_row,  clicked_col):
                if player == 1:
                    mark_screen(clicked_row,  clicked_col, 1)
                    c+=1
                    if win_line(player):
                        draw_winner(player)
                        end_game = True
                    player = 2
                    if c == 9 and not end_game:
                        font = pygame.font.SysFont(None, 40)
                        winner = "No one wins !!"
                        win_color = font.render(winner, True, "red")
                        pygame.draw.rect(WIN, "black", (WIDTH // 2 - 80, HEIGHT // 2 - 90, 200, 60))
                        WIN.blit(win_color, (WIDTH // 2 - 80, HEIGHT // 2 - 90))
                elif player == 2:
                    mark_screen(clicked_row,  clicked_col, 2)
                    c+=1

                    if win_line(player):
                        draw_winner(player)
                        end_game = True

                    player = 1
                    if c == 9 and not end_game:
                        font = pygame.font.SysFont(None, 40)
                        winner = "no one wins !!"
                        win_color = font.render(winner, True, "red")
                        pygame.draw.rect(WIN, "black", (WIDTH // 2 - 80, HEIGHT // 2 - 90, 200, 60))
                        WIN.blit(win_color, (WIDTH // 2 - 80, HEIGHT // 2 - 90))

                draw_shape()


    pygame.display.update()
