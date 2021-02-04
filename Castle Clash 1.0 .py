import pygame
import random
import sys
import time

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("城堡冲突一")
bgImg = pygame.image.load("bg1.png")
loseImg = pygame.image.load("fail.png")
sucImg = pygame.image.load("success.png")

    def __init__(self)
        self.hp = 1000
        self.way = "left"
        self.image = pygame.image.load("hero.png")
        self.rect = pygame.Rect(200, 400, 50, 50)

        

    def move(self, way, num):
        self.way = way
        if self.way == 'up':
            self.rect.y = self.rect.y - num
        elif self.way == 'down':
            self.rect.y = self.rect.y + num
        elif self.way == 'left':
            self.rect.x = self.rect.x - num
        elif self.way == 'right':
            self.rect.x = self.rect.x + num

    def show(self, screen):
        screen.blit(self.image, self.rect)



class Enemy():
    def __init__(self):
        self.way = random.choice(["up", "down", "left", "right"])
        self.image = pygame.image.load("enemy.png")
        x = random.randint(0, 450)
        y = random.randint(0, 450)
        self.rect = pygame.Rect(x, y, 50, 50)

    def move(self, num):
        if self.way == 'up':
            self.rect.y = self.rect.y - num
            if self.rect.y < 0:
                self.way = "down"
        elif self.way == 'down':
            self.rect.y = self.rect.y + num
            if self.rect.y > 450:
                self.way = "up"
        elif self.way == 'left':
            self.rect.x = self.rect.x - num
            if self.rect.x < 0:
                self.way = "right"
        elif self.way == 'right':
            self.rect.x = self.rect.x + num
            if self.rect.x > 450:
                self.way = "left"

    def show(self, screen):
        screen.blit(self.image, self.rect)

    def hit(self, h):
        if self.rect.colliderect(h.rect):
            h.hp = h.hp - 50

hero = Hero()

enemiesNum = 10
enemiesList = []

for i in range(enemiesNum):
    enemy = Enemy()
    enemiesList.append(enemy)



win = 2
t1 = time.time()

while True:
    screen.blit(bgImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero.move("right", 50)
            elif event.key == pygame.K_LEFT:
                hero.move("left", 50)
            elif event.key == pygame.K_UP:
                hero.move("up", 50)
            elif event.key == pygame.K_DOWN:
                hero.move("down", 50)

    hero.show(screen)

    for m in enemiesList:
        m.move(1)
        m.show(screen)
        m.hit(hero)
        time.sleep(0.01)

    if hero.hp <= 0:
        win = 0
        break
    t2 = time.time()
    if t2 - t1 >= 60:
        win = 1
        break
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if win == 1:
        screen.blit(sucImg, (0, 0))
    if win == 0:
        screen.blit(loseImg, (0, 0))
    pygame.display.update()
