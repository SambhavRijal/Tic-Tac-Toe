import pygame
import random
import os
import time

pygame.init()
pygame.font.init()

# Main Window
width = 600
height = 600
win = pygame.display.set_mode((width, height))

# Title and Icon
pygame.display.set_caption("Tic Tac Toe")


def draw_board():
    first = pygame.draw.rect(win, (255, 255, 255), (0, 0, 198, 198))
    second = pygame.draw.rect(win, (255, 255, 255), (201, 0, 198, 198))
    third = pygame.draw.rect(win, (255, 255, 255), (402, 0, 198, 198))
    fourth = pygame.draw.rect(win, (255, 255, 255), (0, 201, 198, 198))
    fifth = pygame.draw.rect(win, (255, 255, 255), (201, 201, 198, 198))
    sixth = pygame.draw.rect(win, (255, 255, 255), (402, 201, 198, 198))
    seventh = pygame.draw.rect(win, (255, 255, 255), (0, 402, 198, 198))
    eighth = pygame.draw.rect(win, (255, 255, 255), (201, 402, 198, 198))
    ninth = pygame.draw.rect(win, (255, 255, 255), (402, 402, 198, 198))
    clicks = ['', first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]
    return clicks


def is_winner(b, le):
    if b[1] == le and b[2] == le and b[3] == le or b[4] == le and b[5] == le and b[6] == le or b[7] == le and b[
        8] == le and b[9] == le or b[1] == le and b[4] == le and b[7] == le or b[2] == le and b[5] == le and b[
        8] == le or b[3] == le and b[6] == le and b[9] == le or b[1] == le and b[5] == le and b[9] == le or b[
        3] == le and b[5] == le and b[7] == le:
        return 1


def safe_AI(b, le, ce):
    if b[1] == ce and b[3] == ce and b[2] == ' ':
        return 2
    elif b[4] == ce and b[6] == ce and b[5] == ' ':
        return 5
    elif b[7] == ce and b[9] == ce and b[8] == ' ':
        return 8
    elif b[1] == ce and b[7] == ce and b[4] == ' ':
        return 4
    elif b[2] == ce and b[8] == ce and b[5] == ' ':
        return 5
    elif b[3] == ce and b[9] == ce and b[6] == ' ':
        return 6
    elif b[1] == ce and b[9] == ce and b[5] == ' ':
        return 5
    elif b[3] == ce and b[7] == ce and b[5] == ' ':
        return 5
    elif b[1] == ce and b[2] == ce and b[3] == ' ':
        return 3
    elif b[4] == ce and b[5] == ce and b[6] == ' ':
        return 6
    elif b[7] == ce and b[8] == ce and b[9] == ' ':
        return 9
    elif b[2] == ce and b[3] == ce and b[1] == ' ':
        return 1
    elif b[5] == ce and b[6] == ce and b[4] == ' ':
        return 4
    elif b[8] == ce and b[9] == ce and b[7] == ' ':
        return 7
    elif b[1] == ce and b[4] == ce and b[7] == ' ':
        return 7
    elif b[2] == ce and b[5] == ce and b[8] == ' ':
        return 8
    elif b[3] == ce and b[6] == ce and b[9] == ' ':
        return 9
    elif b[7] == ce and b[4] == ce and b[1] == ' ':
        return 1
    elif b[8] == ce and b[5] == ce and b[2] == ' ':
        return 2
    elif b[9] == ce and b[6] == ce and b[3] == ' ':
        return 3
    elif b[1] == ce and b[5] == ce and b[9] == ' ':
        return 9
    elif b[5] == ce and b[9] == ce and b[1] == ' ':
        return 1
    elif b[3] == ce and b[5] == ce and b[7] == ' ':
        return 7
    elif b[7] == ce and b[5] == ce and b[3] == ' ':
        return 3
    elif b[1] == le and b[3] == le and b[2] == ' ':
        return 2
    elif b[4] == le and b[6] == le and b[5] == ' ':
        return 5
    elif b[7] == le and b[9] == le and b[8] == ' ':
        return 8
    elif b[1] == le and b[7] == le and b[4] == ' ':
        return 4
    elif b[2] == le and b[8] == le and b[5] == ' ':
        return 5
    elif b[3] == le and b[9] == le and b[6] == ' ':
        return 6
    elif b[1] == le and b[9] == le and b[5] == ' ':
        return 5
    elif b[3] == le and b[7] == le and b[5] == ' ':
        return 5
    elif b[1] == le and b[2] == le and b[3] == ' ':
        return 3
    elif b[4] == le and b[5] == le and b[6] == ' ':
        return 6
    elif b[7] == le and b[8] == le and b[9] == ' ':
        return 9
    elif b[2] == le and b[3] == le and b[1] == ' ':
        return 1
    elif b[5] == le and b[6] == le and b[4] == ' ':
        return 4
    elif b[8] == le and b[9] == le and b[7] == ' ':
        return 7
    elif b[1] == le and b[4] == le and b[7] == ' ':
        return 7
    elif b[2] == le and b[5] == le and b[8] == ' ':
        return 8
    elif b[3] == le and b[6] == le and b[9] == ' ':
        return 9
    elif b[7] == le and b[4] == le and b[1] == ' ':
        return 1
    elif b[8] == le and b[5] == le and b[2] == ' ':
        return 2
    elif b[9] == le and b[6] == le and b[3] == ' ':
        return 3
    elif b[1] == le and b[5] == le and b[9] == ' ':
        return 9
    elif b[5] == le and b[9] == le and b[1] == ' ':
        return 1
    elif b[3] == le and b[5] == le and b[7] == ' ':
        return 7
    elif b[7] == le and b[5] == le and b[3] == ' ':
        return 3
    else:
        while True:
            loc = random.randint(1, 9)
            if b[loc] == ' ':
                return loc
                break


#clicks = draw_board()


def clickcheck(clicks, click, p):
    for i in clicks[1:]:
        if i.collidepoint(click):
            lspos = clicks.index(i)
            print(f"{i} {lspos}clicked")
            if b[lspos] == ' ':
                pygame.draw.rect(win, (255, 0, 0), (i[0] + 10, i[1] + 10, i[2] - 30, i[3] - 30))
                b[lspos] = p[0]
                a.append(lspos)
                print(a)
                print(b)


def computermove(b, p):
    while True:
        risk = safe_AI(b, p[0], p[1])
        i = clicks[risk]
        time.sleep(0)
        pygame.draw.rect(win, (0, 255, 0), (i[0] + 10, i[1] + 10, i[2] - 30, i[3] - 30))
        b[risk] = p[1]
        a.append(risk)
        break


def end_menu(win, status):
    x, y = pygame.display.get_surface().get_size()
    win.fill((255, 255, 255))
    myfont = pygame.font.SysFont("Comic Sans MS", 50)
    textsurface = myfont.render(f'You {status}', False, (0, 0, 0))
    win.blit(textsurface, (x / 2 - 60, y - (y - 10)))
    pygame.draw.rect(win, (255, 0, 0), (100, 100, 80, 50))


def game_won(win):
    status = 'Won'
    end_menu(win, status)
    print(" ")
    print(" ")
    print("***** Congrats you won *****")
    print(" ")


def game_lost(win):
    status = 'Lost'
    end_menu(win, status)
    print(" ")
    print("***** Sorry you lost!!!! *****")
    print(" ")


def game_tie(win):
    status = 'Tied'
    end_menu(win, status)
    print(" ")
    print("***** Its a Tie!!!! *****")
    print(" ")


def update():
    pygame.display.update()

def menu():
    while True:
        nth=0
        win.fill((255, 255, 255))
        p1 = pygame.draw.rect(win, (0, 255, 0), (100, 100, 80, 50))
        p2 = pygame.draw.rect(win, (0, 255, 0), (200, 100, 80, 50))
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                running = False
            if even.type==pygame.MOUSEBUTTONUP:
                position=pygame.mouse.get_pos()
                if p1.collidepoint(position):
                    p=1
                    print(p)
                    return p
                elif p2.collidepoint(position):
                    p=2
                    print(p)
                    return p
                else:
                    nth=0
        update()



pause = "False"
turn = 0
b = [' '] * 10
a = []
p = ('X', 'O')
play = menu()
menu=1
draw=1
if play==1:
    win.fill((0,0,0))
    clicks = draw_board()
# Main Loop
running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if play == 1:
            if len(a) != 9:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if turn == 0:
                        clickcheck(clicks, pos, p)
                        turn = 1

            if len(a) == 9:
                if is_winner(b, p[0]) != 1 and is_winner(b, p[1]) != 1:
                    game_tie(win)
            if turn == 1:
                if len(a) != 9:
                    computermove(b, p)
                    turn = 0
            print(a)
            if is_winner(b, p[0]) == 1:
                game_won(win)
                break
            elif is_winner(b, p[1]) == 1:
                game_lost(win)
                break
            else:
                if len(a) > 9:
                    if is_winner(b, p[1]) == 1:
                        game_lost(win)
                    else:
                        game_tie(win)
                    break

        elif play == 2:
            print("Multiplayer")

    update()
