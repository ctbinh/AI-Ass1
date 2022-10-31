import pygame
import sys

import time
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


class GUI:

    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    MARGIN = 5
    def __init__(self, data, title, callback):
        self.data = data
        self.title = title
        self.cell_width = GUI.SCREEN_WIDTH // len(data) - GUI.MARGIN
        self.cell_height = GUI.SCREEN_HEIGHT // len(data) - GUI.MARGIN
        self.call_back = callback
    def init_game(self):

        pygame.init()
        
        self.font = pygame.font.SysFont('Arial', 25)
        self.surface = pygame.display.set_mode((GUI.SCREEN_WIDTH, GUI.SCREEN_HEIGHT))
        pygame.display.set_caption(self.title)
        self.surface.fill(WHITE)
        self.clock = pygame.time.Clock()
        self.main_loop()

    def update_data(self, data):
        self.data = data
        
        self.display_data()
    
    def display_data(self):
        
        

        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                pygame.draw.rect(self.surface,
                             GREEN,
                             [(self.cell_width + GUI.MARGIN) * col + GUI.MARGIN,
                              (self.cell_height + GUI.MARGIN) * row + GUI.MARGIN,
                              self.cell_width,
                              self.cell_height])
                
                self.surface.blit(self.font.render(self.data[row][col], True, (255,0,0))
                , (self.cell_width * col + self.cell_width // 2 - GUI.MARGIN
                , self.cell_height * row + self.cell_height // 2 - GUI.MARGIN))
        
        self.clock.tick(60)
        pygame.display.flip()
                    
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.call_back(-1)
                    if event.key == pygame.K_RIGHT:
                        self.call_back(1)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.call_back(0)
            self.display_data()
            
    def go_to_step(self, index):
        pass

    def dislay_grid(self):
        pass


class GameManager:

    def __init__(self, title, init_state, list_data):
        
        
        self.list_data = list_data
        self.GUI = GUI(init_state, title, self.display_data)
        self.index = 0
        self.GUI.init_game()
         
    def display_data(self, step):
        
        if step == 0:
            self.GUI.update_data(self.list_data[len(self.list_data) - 1])
        elif self.index + step < len(self.list_data) and self.index + step >= 0:
            self.index += step
            self.GUI.update_data(self.list_data[self.index])
            
        


    