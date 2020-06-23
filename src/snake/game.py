# Core imports
import os, sys, pygame

# Local imports

from config import cfg_dict as cfg
from global_store import global_dict as glo
from global_store import input_dict, input_memory_dict

class Main():
    
    def __init__(self):
        
        glo['main'] = self   # Reference main object in globals
        self.window_obj_dict = {}  # Define window object dictionary
        self.background_color = cfg['background_color']
        
        # Initialise pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((cfg['disp_width'], cfg['disp_height']))
        pygame.display.set_caption(cfg['caption'])
        
        # Run loop
        self.loop()
        
        # Exit at end of loop
        pygame.quit()
            
        
    def loop(self):
        
        self.exit = False
        
        while not self.exit:
            self.check_events()
            self.apply_input()
            self.update_windows()
            self.store_input_memory()
            self.clock.tick(60)
        
        
    def check_events(self):
        """
        Check the events list one by one for input / exitting.
        """
        
        # Check mouse position and buttons
        input_dict['mouse_x'], input_dict['mouse_y'] = pygame.mouse.get_pos()
        input_dict['mouse_0'], input_dict['mouse_1'], input_dict['mouse_2'] = pygame.mouse.get_pressed()
            
        # Re-initialise mouse scrolls
        input_dict['mouse_scroll_up'] = False
        input_dict['mouse_scroll_down'] = False
        
        # Check over incoming events
        for event in pygame.event.get():
            
            # Check for quit event
            if event.type == pygame.QUIT:
                self.exit = True
                print(event)
                
            # Key-press events
            elif event.type == pygame.KEYDOWN:
                if event.key in input_dict.keys():
                    input_dict[event.key] = True
                    
            # Key-release events
            elif event.type == pygame.KEYUP:
                if event.key in input_dict.keys():
                    input_dict[event.key] = False
                    
            # Mouse scroll events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    input_dict['mouse_scroll_up'] = True
                elif event.button == 5:
                    input_dict['mouse_scroll_down'] = True
                    
                    
    def apply_input(self):
        pass
        
    
    def store_input_memory(self):
        
        for key, value in input_dict.items():
            input_memory_dict[key] = value
    
    
    def update_windows(self):
        
        self.display.fill(self.background_color)
        
        for window_obj in self.window_obj_dict.values():
            if window_obj.active:
                window_obj.update()
                
        pygame.display.update()
        

if __name__ == '__main__':
    main = Main()
