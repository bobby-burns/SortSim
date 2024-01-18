import pygame
import sys
import inspect

import algorithims as algs

class Main:
    def __init__(self):
        # Load all the algorithims
        classes = []
        for _,obj in inspect.getmembers(algs):
            if inspect.ismodule(obj):
                for name,obj in inspect.getmembers(obj):
                    if inspect.isclass(obj) and name != "SortableArray":
                        classes.append(obj)

        self.algorithms = [i() for i in classes]


        # current algorithim
        self.arr = self.algorithms[0]


        # Dropdown menu state
        self.highlightId = -1
        self.isDropDownSelected = False



        # pygame stuff
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        # Some fonts
        self.font = pygame.font.SysFont("", 36)
        self.s_font = pygame.font.SysFont("", 24)

    def render(self):
    

        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill("black")

        # RENDER YOUR GAME HERE
        pygame.draw.rect(self.screen,
                         (47,47,47),
                         (0,0,1280,50))

        self.arr.draw()
        self.dropDownMenu()


        txt = self.font.render("Sorting Simulator",True,(255,255,255))
        self.screen.blit(txt,(5,25 - int(self.font.get_height()/2)))
        self.drawStats()
        

        # flip() the display to put your work on screen
        pygame.display.flip()

        self.clock.tick(60)  # limits FPS to 60

    def run(self):
        while self.running:
            self.events()
            self.render()
        pygame.quit()
        sys.exit(0)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.arr.isSorting = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s]:
                    self.arr.scramble()
                elif keys[pygame.K_b]:
                    self.arr.sim_sort()
                elif keys[pygame.K_SPACE]:
                    self.arr.stop_sim()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
                maxLen = 40 + len(self.algorithms) * 30 
                if mpos[0] >= 1000 and mpos[0] <= 1270 and mpos[1] >= 10 and mpos[1] <= 40:
                    self.isDropDownSelected = not self.isDropDownSelected
                elif self.isDropDownSelected and mpos[0] >= 1000 and mpos[0] <= 1270 and mpos[1] >= 40 and mpos[1] <= maxLen:
                    id = (mpos[1] - 40) // 30
                    self.arr.stop_sim()
                    self.arr = self.algorithms[id]
                    self.isDropDownSelected = False
        if self.isDropDownSelected:
            maxLen = 40 + len(self.algorithms) * 30 
            mpos = pygame.mouse.get_pos()
            if mpos[0] >= 1000 and mpos[0] <= 1270 and mpos[1] >= 40 and mpos[1] <= maxLen:
                self.highlightId = (mpos[1] - 40) // 30




    def drawStats(self):
        acc = self.s_font.render("Accesses: "+str(self.arr.arrayAccesses),True,(255,255,255))
        comp = self.s_font.render("Comparisons: "+str(self.arr.comparisons),True,(255,255,255))
        swaps = self.s_font.render("Swaps: "+str(self.arr.swaps),True,(255,255,255))
        
        height = 25 - self.s_font.get_height()//2

        self.screen.blit(acc,(250,height))
        self.screen.blit(comp,(400,height))
        self.screen.blit(swaps,(580,height))

    def dropDownMenu(self):
        # render background
        pygame.draw.rect(self.screen,(27,27,27),(1000,10,270,30))

        # render triangle
        pygame.draw.polygon(self.screen,
                            (255,255,255),
                            [(1255,22),(1265,22),(1260,27)]
                            )

        # render label
        label = self.s_font.render("Alogorithm:",True,(255,255,255))
        width = 1000 - label.get_width() - 10
        self.screen.blit(label,(width,18))

        # render selected algorithm
        algo = self.s_font.render(self.arr.__class__.__name__,True,(255,255,255))
        self.screen.blit(algo,(1010,18))

        # render dropdown when selected
        if self.isDropDownSelected:
            for i,v in enumerate(self.algorithms):
                color = (27,27,27)
                if self.highlightId == i:
                    color = (67,67,67)
                pygame.draw.rect(self.screen,color,
                                (1000, 40 + (30*(i)),270,30)
                                 )
                txt = self.s_font.render(v.__class__.__name__,True,(255,255,255))
                self.screen.blit(txt,(1010,18 + (30*(i+1))))


 
if __name__ == "__main__":
    App = Main()
    App.run()
