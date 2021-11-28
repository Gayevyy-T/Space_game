import pygame
import os
pygame.font.init() # to show text in different font
pygame.mixer.init() # to initialize sound library

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))#window size
pygame.display.set_caption("space_game") #give the name of the popped up window 

WHITE = (255, 255, 255) #set the color (white has these param)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60

FONT = pygame.font.SysFont("calibri", 50)

POINTER_IMAGE = pygame.image.load(os.path.join("Assets","pointer.png"))
POINTER = pygame.transform.scale(POINTER_IMAGE, (55, 40)) #resize ship to 55 width and 40 height

def draw_window():
    WIN.fill(YELLOW) #fill the popped up window to white
#     WIN.blit(SPACE, (0, 0)) #pasting the space immage to the game
#     '''pygame.draw.rect(WIN, BLACK, BORDER) #draw rect in the WINdow; COLOR; what we draw(somewhere defined rect)'''
    choose = pygame.font.SysFont("calibri", 55).render("PLEASE CHOOSE THE PLAYER:", 1, BLACK)
    option1 = FONT.render("Player 1", 1, BLACK)
    option2 = FONT.render("Player 2", 1, BLACK)
    WIN.blit(choose, (150, 130))
    WIN.blit(option1, (200, 200))
    WIN.blit(option2, (200, 250))

#     keys_pressed = pygame.key.get_pressed()
#     st = WIN.blit(POINTER, (200 - 60, 200))
#     nd = WIN.blit(POINTER, (200 - 60, 250))
#     if keys_pressed[pygame.K_DOWN]:
        

#     ### '''WIN.blit(YELLOW_SPACESHIP, (300,100)) #blit - to display immage on the screen,(define posiiton(start from top left corner))  "300 -> right & 100 down"'''
#     WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #yellow.x & .y --> take arguments from vars in main -> yellow (100 & 300)
#     WIN.blit(RED_SPACESHIP, (red.x, red.y))

#     for bullet in red_bullets:
#         pygame.draw.rect(WIN, RED, bullet)
#     for bullet in yellow_bullets:
#         pygame.draw.rect(WIN, YELLOW, bullet)    

    pygame.display.update() #update is needed every time when something is changing


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT event is when we press "x" on the popped up window of the game
                run = False     #If change to "True", the game window will be not possible to close
                pygame.quit()
    

            


            draw_window()
            
           

    main() # to start the game again

if __name__ == "__main__":
    main()