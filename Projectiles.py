import pygame
from copy import copy
from Rendering import *
import random

class Bullets:
    def __init__(self):
        self.bullets = list() #list of bullets
        

    def new_bullet(self):
        rect = bullet_img.get_rect() #rect of the curface containing the bullet
        rect.center = (200, 1000) #implement the x-coordinate of the bullet
        self.bullets.append(rect) 

    def manage_bullets(self): 
        for bullet in self.bullets:
            if bullet.y < 0:
                self.bullets.remove(bullet) #delete the projectile if it has exceeded the boundary
        for bullet in self.bullets: #move the projectile up by 10
            bullet.y -= 10

    def draw_bullets(self):
        for bullet_coord in self.bullets:
            screen.blit(bullet_img, bullet_coord) #blit the bullet png at the coordinate

class Rocks:
    def __init__(self):
        self.rocks = list()
    
    def new_rock(self):
        #implement the calculations later, for now keep it as 0
        rock_attributes = {"size": 0, "rotation": 0, "angular_velocity": 1, "v_x": 10, "v_y": 0, "x": 200, "y": 50, "value": 0}   
        rock_image = rock_img[0] #implement the other colors later
        rock_combined = [rock, rock_attributes, rock_image]
        self.rocks.append(rock_combined) #each element in the list rocks will be a list with 2 elements: [0] rock surface with no transformations, [1] is the attributes, [2] is the rock surface with the transformations 

    def update_position(self):
        for i in self.rocks:
            i[1]["rotation"] = (i[1]["rotation"] + i[1]["angular_velocity"])%360 #add the angular velocity to the angle
            i[0] = pygame.transform.scale(i[0], (150, 150)) #implement scaling calculation later
            i[2] = pygame.transform.rotate(i[0], i[1]["rotation"]) #rotation
            i[1]["x"] += i[1]["v_x"] #update x 
            i[1]["y"] += i[1]["v_y"] #update y
            #check left and right bounce
            rock_mask = pygame.mask.from_surface(i[2]) 
            offset_l = (screen_l_rect.left - (i[1]["x"]-0.5*i[2].get_width()), screen_l_rect.top - (i[1]["y"]-0.5*i[2].get_height()))
            offset_r = (screen_r_rect.left - (i[1]["x"]-0.5*i[2].get_width()), screen_r_rect.top - (i[1]["y"]-0.5*i[2].get_height()))
            if rock_mask.overlap(screen_l_mask, offset_l) or rock_mask.overlap(screen_r_mask, offset_r):
                i[1]["v_x"] *= -1

            #check ground bounce
            offset_b = (screen_b_rect.left - (i[1]["x"]-0.5*i[2].get_width()), screen_b_rect.top - (i[1]["y"]-0.5*i[2].get_height()))
            if rock_mask.overlap(screen_b_mask, offset_b):
                i[1]["v_y"] *= -1
            #gravity
            else:
                i[1]["v_y"] += 0.25

    """def get_outline(self, color=(255,255,255)):
        #return outlined image of the same size for testing purposes
        #for collision detection just return the mask
        mask = pygame.mask.from_surface(self.rocks[0][2]) 
        outline = mask.outline()

        
        #return mask
        #print(outline)
        #outline_image = pygame.Surface((image.get_width(), image.get_height())).convert_alpha()
        #outline_image.fill((0,0,0,0))
        #for point in outline:
         #   outline_image.set_at(point,color)
        #return outline_image"""

    
    def collision_test(self, bullets, bullet_class):
        for rock in self.rocks:
            for bullet in bullets:
                offset = (bullet.left - (rock[1]["x"]-0.5*rock[2].get_width()), bullet.top - (rock[1]["y"]-0.5*rock[2].get_height()))
                bullet_mask = pygame.mask.from_surface(bullet_img)
                rock_mask = pygame.mask.from_surface(rock[2])
                if rock_mask.overlap(bullet_mask, offset):
                    bullet_class.bullets.remove(bullet)
        

    def draw_rocks(self):
        for i in self.rocks:
            screen.blit(i[2], (i[1]["x"]-0.5*i[2].get_width(), i[1]["y"]-0.5*i[2].get_height())) #surface, (x, y)

    def check_collision_player(self):
        pass

    def check_collision_bullet(self):
        pass


