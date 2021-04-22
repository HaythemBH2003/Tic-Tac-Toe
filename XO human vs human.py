import numpy
import pygame
import sys

player = 1

BackGround = (0, 172, 238)
BoardColor = (255, 255, 255)
Xcolor = (57, 255, 20)
Ocolor = (177, 156, 217)

board = numpy.zeros((3, 3))
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("                                                                                Xs & Os")
screen.fill(BackGround)


def draw_board():
    pygame.draw.line(screen, BoardColor, (20, 200), (580, 200), 10)
    pygame.draw.line(screen, BoardColor, (20, 400), (580, 400), 10)
    pygame.draw.line(screen, BoardColor, (200, 20), (200, 580), 10)
    pygame.draw.line(screen, BoardColor, (400, 20), (400, 580), 10)


draw_board()


def mark_board(row, col, player):
    board[row, col] = player


def check_square(row, col):
    return board[row, col] == 0


def board_is_full():
    for i in range(3):
        for j in range(3):
            if board[i, j] == 0:
                return False


def mark_position(row, col, player):
    if player == 1:
        pygame.draw.line(screen, Xcolor, (col*200+20, row*200+20), (col*200+180, row*200+180), 10)
        pygame.draw.line(screen, Xcolor, (col * 200 + 20, row * 200 + 180), (col * 200 + 180, row * 200 + 20), 10)
    if player == 2:
        pygame.draw.circle(screen, Ocolor, (col*200+100, row*200+100), 80, 10)


def check_win():
    # checking horizontal win #
    for win_row in range(3):
        if board[win_row, 0] == board[win_row, 1] == board[win_row, 2] and board[win_row, 0] == 1:
            pygame.draw.line(screen, Xcolor, (10, win_row*200+100), (590, win_row*200+100), 15)
            return True
        if board[win_row, 0] == board[win_row, 1] == board[win_row, 2] and board[win_row, 0] == 2:
            pygame.draw.line(screen, Ocolor, (10, win_row*200+100), (590, win_row*200+100), 15)
            return True
    # checking vertical win #
    for win_col in range(3):
        if board[0, win_col] == board[1, win_col] == board[2, win_col] and board[0, win_col] == 1:
            pygame.draw.line(screen, Xcolor, (win_col*200+100, 10), (win_col*200+100, 590), 15)
            return True
        if board[0, win_col] == board[1, win_col] == board[2, win_col] and board[0, win_col] == 2:
            pygame.draw.line(screen, Ocolor, (win_col*200+100, 10), (win_col*200+100, 590), 15)
            return True
    # checking diagonal ascending win #
    if board[2, 0] == board[1, 1] == board[0, 2] == 1:
        pygame.draw.line(screen, Xcolor, (10, 590), (590, 10), 15)
        return True
    if board[2, 0] == board[1, 1] == board[0, 2] == 2:
        pygame.draw.line(screen, Ocolor, (10, 590), (590, 10), 15)
        return True
    # checking diagonal descending win #
    if board[0, 0] == board[1, 1] == board[2, 2] == 1:
        pygame.draw.line(screen, Xcolor, (10, 10), (590, 590), 15)
        return True
    if board[0, 0] == board[1, 1] == board[2, 2] == 2:
        pygame.draw.line(screen, Ocolor, (10, 10), (590, 590), 15)
        return True


def restart():
    player = 1
    screen.fill(BackGround)
    draw_board()
    for i in range(3):
        for j in range(3):
            board[i, j] = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseX = event.pos[0]
            MouseY = event.pos[1]
            col = MouseX//200
            row = MouseY//200
            check_win()
            if check_square(row, col) and (not board_is_full()) and check_win() != True:
                if player == 1:
                    mark_board(row, col, player)
                    print(board)
                    mark_position(row, col, player)
                    player = 2
                elif player == 2:
                    mark_board(row, col, player)
                    print(board)
                    mark_position(row, col, player)
                    player = 1
            check_win()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
    pygame.display.update()
