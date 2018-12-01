import pygame
import random
import math
import matplotlib.pyplot as plt
import pylab as pl
import time 
import subprocess 
import pandas as pd 
from inference import * 

DATA_FOLDER = 'rawData/'

background_colour = (255,255,255)
(width, height) = (480, 350)
size = 15
numlevels = 11 
testing = True
pygame.init()

def addVectors(vec):
    x  = math.sin(vec[0]) * vec[1] 
    y  = math.cos(vec[0]) * vec[1] 
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def collide(particle, block, collision=False):
    # right bounce
    if  block.x > particle.x > block.x - particle.size:
        if block.y < particle.y < block.y + block.size[1]: 
            particle.x = block.x - particle.size
            particle.angle = - particle.angle 
            collision = True 

    # left bounce 
    elif block.x + block.size[0] < particle.x < block.x + block.size[0] + particle.size: 
        if block.y < particle.y < block.y + block.size[1]: 
            particle.x =  block.x + block.size[0] + particle.size 
            particle.angle = - particle.angle
            collision = True 

    # up bounce 
    elif block.y > particle.y > block.y - particle.size: 
        if block.x < particle.x < block.x + block.size[0]: 
            particle.y = block.y - particle.size 
            particle.angle = math.pi - particle.angle 
            collision = True 

    # down bounce 
    elif block.y + block.size[1] < particle.y < block.y + block.size[1] + particle.size: 
        if block.x < particle.x < block.x + block.size[0]: 
            particle.y = block.y + block.size[1] + particle.size 
            particle.angle = math.pi - particle.angle 
            collision = True 

    return collision 

def getDecisionTime(ts, red, green):
    for t in range(len(ts)): 
        if red[t] >= 0.5 or green[t] >= 0.5: 
            # print (ts[t]/ts[-1])
            return (ts[t]/ts[-1])

def plotDist(ts, red, green, unsure): 
    plt.plot(ts, red, 'r-', label='Red Block')
    plt.plot(ts, green, 'g-', label='Green Block')
    plt.plot(ts, unsure, 'b-', label='Unsure')
    plt.ylabel('Probability')
    plt.xlabel('Time')
    plt.legend(loc='best')
    plt.title('Block Collision Probability for Intuitive Physics Simulator')
    plt.show()

def totalTime(timeline): 
    count = 0 
    for button_type, t in timeline: 
        count += t
    return count 

def requestName():
    name = input('Please Enter Your Kerberos: ')
    return str(name)

def createOutput(name):
    CSV_CMD = 'touch'
    for l in range(numlevels):
        CSV_CMD += ' ' + DATA_FOLDER + name + str(l) + '.csv'

    subprocess.check_output(CSV_CMD, shell=True)

def writeOutput(level, ts, timeline):
    def getStatus(t, d):
        for status, timing in timeline: 
            if t < timing: 
                d['time'].append(round(t, 2))
                d['status'].append(status) 

                break 

    csvFile = DATA_FOLDER + name + str(level) + '.csv'
    t = 0.0 
    d = {'time': list(), 'status': list()}
    while t < ts[-1]: 
        getStatus(t, d)
        t += 0.05

    df = pd.DataFrame(data=d)
    df.sort_values(by=['time'])

    with open(csvFile, 'w') as f: 
        df.to_csv(f)

def level0():
    particle = Particle((10, 30), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((250, 190), (100, 5)), 
                 Wall((400, 120), (5, 100)),
                 Wall((140, 140), (100, 5)), 
                 Wall((135, 145), (5, 100))]

    # target 
    blocks = [Block((300, 30), (30, 80), (200, 0, 0), 'red'), 
              Block((50, 160), (30, 80), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level1():
    particle = Particle((10, 30), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((300, 220), (100, 5)), 
                 Wall((400, 120), (5, 100)),
                 Wall((180, 80), (100, 5)), 
                 Wall((120, 170), (100, 5))]

    # target 
    blocks = [Block((320, 50), (30, 80), (200, 0, 0), 'red'), 
              Block((50, 130), (30, 80), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level2():
    particle = Particle((10, 30), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((180, 190), (100, 5)), 
                 Wall((280, 90), (5, 100)),
                 Wall((180, 85), (100, 5)), 
                 Wall((175, 90), (5, 100))]

    # target 
    blocks = [Block((195, 100), (30, 80), (200, 0, 0), 'red'), 
              Block((50, 160), (30, 80), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level3():
    particle = Particle((10, 30), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((300, 220), (100, 5)), 
                 Wall((230, 90), (5, 100)),
                 Wall((55, 80), (100, 5)), 
                 Wall((110, 200), (100, 5))]

    # target 
    blocks = [Block((50, 120), (30, 80), (200, 0, 0), 'red'), 
              Block((300, 50), (30, 80), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level4():
    particle = Particle((50, 50), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((280, 240), (100, 5)), 
                 Wall((400, 40), (5, 100)),
                 Wall((30, 200), (100, 5)), 
                 Wall((240, 100), (5, 100))]

    # target 
    blocks = [Block((300, 30), (30, 80), (200, 0, 0), 'red'), 
              Block((60, 110), (80, 30), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level5():
    particle = Particle((10, 30), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((50, 240), (100, 5)), 
                 Wall((95, 120), (5, 100)),
                 Wall((100, 80), (100, 5)), 
                 Wall((170, 220), (100, 5))]

    # target 
    blocks = [Block((130, 95), (30, 80), (200, 0, 0), 'red'), 
              Block((185, 180), (80, 30), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level6():
    particle = Particle((240, 60), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((360, 30), (100, 5)), 
                 Wall((70, 160), (5, 100)),
                 Wall((80, 120), (100, 5)), 
                 Wall((260, 210), (100, 5))]

    # target 
    blocks = [Block((150, 30), (30, 80), (200, 0, 0), 'red'), 
              Block((90, 150), (30, 80), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level7():
    particle = Particle((300, 200), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((30, 40), (100, 5)), 
                 Wall((400, 100), (5, 100)),
                 Wall((95, 100), (100, 5)), 
                 Wall((170, 210), (100, 5))]

    # target 
    blocks = [Block((20, 150), (80, 30), (200, 0, 0), 'red'), 
              Block((115, 170), (30, 80), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level8():
    particle = Particle((30, 210), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((410, 120), (5, 100)),
                 Wall((30, 80), (100, 5)), 
                 Wall((190, 60), (100, 5))]

    # target 
    blocks = [Block((240, 130), (30, 80), (200, 0, 0), 'red'), 
              Block((150, 160), (30, 80), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level9():
    particle = Particle((65, 220), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((170, 230), (100, 5)), 
                 Wall((395, 150), (5, 100)),
                 Wall((40, 130), (100, 5)), 
                 Wall((130, 85), (100, 5))]

    # target 
    blocks = [Block((100, 30), (80, 30), (200, 0, 0), 'red'), 
              Block((320, 150), (30, 80), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

def level10():
    particle = Particle((300, 40), size)
    particle.speed = 4
    particle.angle = math.pi * 1 / 4 

    obstacles = [Wall((170, 200), (100, 5)), 
                 Wall((390, 150), (5, 100)),
                 Wall((20, 100), (100, 5)), 
                 Wall((120, 80), (100, 5))]

    # target 
    blocks = [Block((190, 30), (80, 30), (200, 0, 0), 'red'), 
              Block((70, 160), (80, 30), (0, 150, 0), 'green')]

    return particle, obstacles, blocks

class Particle():
    def __init__(self, pos, size):
        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 0
        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed))
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounceEdge(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle

    def bounceWall(self, wall): 
        collide(self, wall)

class Wall():
    def __init__(self, pos, size):
        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.color = (0, 0, 0)
        self.thickness = 0

    def display(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size[0], self.size[1]], self.thickness)

class Block():
    def __init__(self, pos, size, color, name): 
        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.color = color
        self.thickness = 0
        self.name = name 

    def display(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size[0], self.size[1]], self.thickness)

levels = [level0(), level1(), level2(), level3(), level4(), level5(), 
        level6(), level7(), level8(), level9(), level10()]

if testing: 
    name = requestName()
    createOutput(name)

dt = list() 

for l in range(len(levels)):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Dynamics Intuitive Physics Simulator')
    red_button = pygame.Rect(60, 290, 150, 40)
    green_button = pygame.Rect(270, 290, 150, 40)
    next_button = pygame.Rect(165, 150, 150, 40)

    font = pygame.font.SysFont("comicsansms", 16)
    redText = font.render("Red Block", True, (0, 0, 0))
    greenText = font.render("Green Block", True, (0, 0, 0))
    nextText = font.render("Next", True, (0, 0, 0))

    # wall 
    my_walls = [Wall((0, 0), (width, 5)), 
                Wall((0, height-85), (width, 5)),
                Wall((0, 0), (5, height-80)),
                Wall((width-5, 0), (5, height-80))]

    particle, my_obstacles, my_blocks = levels[l]

    running = True
    before_next = True 
    prev = 'none'
    ts, red, green, unsure, timeline, timedist, level_dist = \
        list(), list(), list(), list(), list(), list(), list() 

    if l == 0: 
        start_game = True 
        start_button = pygame.Rect(165, 150, 150, 40)
        startText = font.render("Start", True, (0, 0, 0))
        while start_game: 
            screen.fill(background_colour)
            pygame.draw.rect(screen, (100, 180, 255), start_button)
            screen.blit(startText, (220, 157.5))

            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    mouse_pos = event.pos 

                    if start_button.collidepoint(mouse_pos):
                        start_game = False 

            pygame.display.flip()

    button_start = time.time() 
    start = time.time() 


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = event.pos 

                if red_button.collidepoint(mouse_pos):
                    red_time = time.time()
                    timedist.append(('unsure', red_time - button_start))
                    timeline.append(('unsure', red_time - start))
                    prev = 'red'

                if green_button.collidepoint(mouse_pos):
                    green_time = time.time() 
                    timedist.append(('unsure', green_time - button_start))
                    timeline.append(('unsure', green_time - start))
                    prev = 'green'

            if event.type == pygame.MOUSEBUTTONUP:
                if prev == 'red':
                    button_start = time.time() 
                    timedist.append(('red', button_start - red_time))
                    timeline.append(('red', button_start - start))

                elif prev == 'green':
                    button_start = time.time() 
                    timedist.append(('green', button_start - green_time))
                    timeline.append(('green', button_start - start))


        ts.append(time.time()-start)

        screen.fill(background_colour)

        # button display 
        pygame.draw.rect(screen, (255, 0, 0), red_button)
        screen.blit(redText, (100, 297.5))
        pygame.draw.rect(screen, (0, 200, 0), green_button)
        screen.blit(greenText, (300, 297.5))

        particle.move()
        particle.bounceEdge()
        particle.display()
        for wall in my_walls + my_obstacles:
            particle.bounceWall(wall)
            wall.display()

        for block in my_blocks:
            if collide(particle, block): 
                running = False 
                end = time.time() 
            block.display()

        pygame.display.flip()

        # path = getPaths(particle.x, particle.y, width, height, particle.size, particle.angle, my_walls + my_obstacles, my_blocks)
        dist = getDistribution(particle.x, particle.y, width, height, particle.size, particle.angle, my_walls + my_obstacles, my_blocks)
        red.append(dist['red'])
        green.append(dist['green'])
        unsure.append(dist['none'])

    if len(timeline) == 0: 
        timeline.append(('unsure', end - start))
        timedist.append(('unsure', end - start))
    else: 
        if timeline[-1][0] == 'unsure': 
            if prev == 'red':
                timedist.append(('red', end - red_time))
                timeline.append(('red', end - start))
            elif prev == 'green':
                timedist.append(('green', end - green_time))
                timeline.append(('green', end - start))

    if testing: 
        writeOutput(l, ts, timeline)
    # level_dist.append((ts, red, green, unsure))
    dt.append(getDecisionTime(ts, red, green))
    # plotDist(ts, red, green, unsure)
    # next button display 

    while before_next: 
        screen.fill(background_colour)
        pygame.draw.rect(screen, (100, 180, 255), next_button)
        screen.blit(nextText, (220, 157.5))

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = event.pos 

                if next_button.collidepoint(mouse_pos):
                    before_next = False 

        pygame.display.flip()



