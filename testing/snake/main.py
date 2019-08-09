import pygame as pg 
from gamesettings import *
from pygame.locals import *
import sys


pg.init()

class Player():

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.player = pg.image.load(EARTH_IMG)

        self.pressedLeft = False
        self.pressedRight = False
        self.pressedUp = False
        self.pressedDown = False

    def update(self):
        if self.pressedLeft == True:
            self.x -= SPEED
        elif self.pressedRight == True:
            self.x += SPEED

    def draw(self, screen):
        screen.blit(self.player,(self.x,self.y))

    def events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.pressedLeft = True
            if event.key == pg.K_RIGHT:
                self.pressedRight = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                self.pressedLeft = False
            if event.key == pg.K_RIGHT:
                self.pressedRight = False
        


class Game():

    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        
        pg.display.set_caption(WINDOW_TITLE)
        self.GAMEOVER = False

        self.FPSClock = pg.time.Clock()
        self.player = Player(PLAYER_START_X, PLAYER_START_Y)

    def run(self):
        
        while not self.GAMEOVER:
            self.screen.fill(pg.color.Color(255,255,255))

            self.eventLoop()
            self.updateGameState()
            self.draw()
            self.FPSClock.tick(FPS)

    def updateGameState(self):
        self.player.update()

    def draw(self):
        self.player.draw(self.screen)
        pg.display.update()


    def eventLoop(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            self.player.events(event)
            
        


g = Game()
g.run()