import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

RED = (255, 0, 0)
BACKGROUND = (153, 51, 51)
WHITE = (255,255,255)
GRAY = (153, 153, 102)
BLACK = (0,0,0)
GREEN = (0,255,0)
DELAY = 50
SPEED = 10

class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,move_x=1,move_y=0,color=RED):
        self.pos = start
        self.move_x = 1
        self.move_y = 0
        self.color = color
        
    def move(self, move_x, move_y):
        self.move_x = move_x
        self.move_y = move_y
        self.pos = (self.pos[0] + self.move_x, self.pos[1] + self.move_y)

    def draw(self, surface, eyes=False):
        distance = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*distance,j*distance, distance, distance))
        if eyes:
            centre = distance//2
            radius = 3
            circleMiddle = (i*distance+centre-radius,j*distance+8)
            circleMiddle2 = (i*distance + distance -radius*2, j*distance+8)
            pygame.draw.circle(surface, BLACK, circleMiddle, radius)
            pygame.draw.circle(surface, BLACK, circleMiddle2, radius)
        

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.move_x = 0
        self.move_y = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.move_x = -1
                    self.move_y = 0
                    self.turns[self.head.pos[:]] = [self.move_x, self.move_y]

                elif keys[pygame.K_RIGHT]:
                    self.move_x = 1
                    self.move_y = 0
                    self.turns[self.head.pos[:]] = [self.move_x, self.move_y]

                elif keys[pygame.K_UP]:
                    self.move_x = 0
                    self.move_y = -1
                    self.turns[self.head.pos[:]] = [self.move_x, self.move_y]

                elif keys[pygame.K_DOWN]:
                    self.move_x = 0
                    self.move_y = 1
                    self.turns[self.head.pos[:]] = [self.move_x, self.move_y]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.move_x == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.move_x == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.move_y == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.move_y == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.move_x,c.move_y)
        
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.move_x = 0
        self.move_y = 1

    def addCube(self):
        tail = self.body[-1]
        direction_x, direction_y = tail.move_x, tail.move_y
        self.body.append(cube((tail.pos[0]-direction_x, tail.pos[1] - direction_y)))
        self.body[-1].move_x = direction_x
        self.body[-1].move_y =direction_y

    def delCube(self):
        if len(self.body) == 1:
            message_box('Score: ' + str(len(s.body)), 'Play again!')
            s.reset((10,10))
        else:
            del self.body[-1]

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    side_length = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + side_length
        y = y + side_length

        pygame.draw.line(surface, WHITE, (x,0),(x,w))
        pygame.draw.line(surface, WHITE, (0,y),(w,y))
        

def redrawWindow(surface):
    global rows, width, s, snack, trap, bombs
    surface.fill(BACKGROUND)
    s.draw(surface)
    snack.draw(surface)
    trap.draw(surface)
    for bomb in bombs:
        bomb.draw(surface)
    drawGrid(width,rows, surface)
    pygame.display.update()


def randomCube(rows, item):
    global bombs, snack, trap
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        Ok = True
        if len(bombs) > 0:
            for bomb in bombs:
                if (x,y) == bomb.pos:
                    Ok = False
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0 or (x,y) == snack.pos or (x,y) == trap.pos or Ok == False:
            continue
        else:
           break
    return (x,y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)


def main():
    global width, rows, s, snack, trap, bombs
    bombs = []
    width = 500
    rows = 20
    first = 0
    win = pygame.display.set_mode((width, width))
    s = snake(RED, (10,10))
    snack = cube((11,13), color=GREEN)
    trap = cube((7,8), color=GRAY)
    
    clock = pygame.time.Clock()
    
    while True:
        pygame.time.delay(DELAY)
        clock.tick(SPEED)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomCube(rows, s), color=GREEN)
        if s.body[0].pos == trap.pos:
            s.delCube()
            trap = cube(randomCube(rows, s), color=GRAY)
        if len(s.body) % 7 == 0:
            first += 1
        else:
            first = 0
        if first == 1:
            bombs.append(cube(randomCube(rows, s), color=BLACK))
        hit_bomb = False
        for bomb in bombs:
            if s.body[0].pos == bomb.pos:
                hit_bomb = True
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])) or hit_bomb:
                message_box('Score: ' + str(len(s.body)), 'Play again!')
                bombs = []
                s.reset((10,10))
                break

        redrawWindow(win)


if __name__ == '__main__':
    main()
