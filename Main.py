from ReadStats import *
from Projectiles import *


def main():

    pygame.init()
    clock = pygame.time.Clock()

    print("hello world")
    run = True

    bullets = Bullets()
    stats = GetStats()
    rocks = Rocks()

    new_bullet = pygame.USEREVENT + 0
    pygame.time.set_timer(new_bullet, 200) #new bullet every 200ms
    manage_projectiles = pygame.USEREVENT + 1
    pygame.time.set_timer(manage_projectiles, 16) #update and check position of bullet every 16ms

    rocks.new_rock()

    player_surf = pygame.Surface((10, 10))
    player_surf.fill('red')
    player_rect = player_surf.get_rect(center = (200, 5000))
    player_mask = pygame.mask.from_surface(player_surf)
    
    angle = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): #quit
                run = False
            elif event.type == new_bullet: #every 200ms
                bullets.new_bullet()
            elif event.type == manage_projectiles: #every 16ms
                bullets.manage_bullets()
                rocks.update_position()
                
        """img_copy = pygame.transform.scale(rock_image[0], (150, 150))
        img_copy = pygame.transform.rotate(img_copy, angle)
        #rock_rect = rock_image.get_rect()
        #rock_rect.center = (200, 500)
        
        screen.blit(img_copy, (200 - img_copy.get_width()/2, 500 - img_copy.get_height()/2))
        #screen.blit(get_outline(img_copy, (255, 255, 255)), (200 - img_copy.get_width()/2, 500 - img_copy.get_height()/2))
        #rocks.draw_rocks()"""

        screen.blit(background, (0, 0))
        rocks.draw_rocks()
        #screen.blit(rocks.get_outline(rocks.rocks[0][2]), (rocks.rocks[0][1]["x"]+100-rocks.rocks[0][2].get_width()/2, rocks.rocks[0][1]["y"]+50-rocks.rocks[0][2].get_height()/2))
        

        rock_img[0] = pygame.transform.scale(rock_img[0], (150, 150))
        rock_image = pygame.transform.rotate(rock_img[0], angle)
        #screen.blit(rock_img[0], (200, 500))
        #screen.blit(rock_image, (200-0.5*rock_image.get_width(), 500-0.5*rock_image.get_height()))
        rock_mask = pygame.mask.from_surface(rock_image)

        offset_x = player_rect.left - (200-0.5*rock_image.get_width())
        offset_y = player_rect.top - (500-0.5*rock_image.get_height())
        if rock_mask.overlap(player_mask, (offset_x, offset_y)):
            #print("collision")
            pass
        else: 
            #print("None")
            pass
            

        bullets.draw_bullets()

        if pygame.mouse.get_pos():
            player_rect.center = pygame.mouse.get_pos()
        screen.blit(player_surf, player_rect)



        rocks.collision_test(bullets.bullets, bullets)
        pygame.display.update()
        clock.tick(60)
        
        angle += 1

        

if __name__ == "__main__":
    main()

pygame.quit()
quit()