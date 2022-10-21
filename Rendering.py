import pygame
#screen
pygame.display.set_caption("aw lord")
screen = pygame.display.set_mode((550, 1200), flags=pygame.RESIZABLE)
background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, (550, 1200))
#bullet
bullet_img = pygame.image.load("bullet.png").convert()
#bullet_img.set_colorkey((0, 0, 0))
bullet_img = pygame.transform.scale(bullet_img, (9, 15))
#rock
rock_img = list() #the list with all the different colored rocks
for i in range(0, 1): #change this number when i finish all the other images
    rock = pygame.image.load("rock"+str(i)+".png").convert()
    rock.set_colorkey((0, 0, 0))
    rock_img.append(rock)
#boundaries
screen_l_surf = pygame.Surface((1, 1200))
screen_l_rect = screen_l_surf.get_rect(center = (0, 600))
screen_l_mask = pygame.mask.from_surface(screen_l_surf)

screen_r_surf = pygame.Surface((1, 1200))
screen_r_rect = screen_r_surf.get_rect(center = (550, 600))
screen_r_mask = pygame.mask.from_surface(screen_r_surf)

screen_b_surf = pygame.Surface((550, 1))
screen_b_rect = screen_b_surf.get_rect(center = (225, 1000))
screen_b_mask = pygame.mask.from_surface(screen_b_surf)




