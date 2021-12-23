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

POINTER_WIDTH, POINTER_HEIGHT = 55, 40
POINTER_IMAGE = pygame.image.load(os.path.join("Assets","pointer.png"))
POINTER = pygame.transform.scale(POINTER_IMAGE, (POINTER_WIDTH, POINTER_HEIGHT)) #resize ship to 55 width and 40 height

def draw_window(pointer_rect):
    WIN.fill(YELLOW) #fill the popped up window to white
#     WIN.blit(SPACE, (0, 0)) #pasting the space immage to the game
#     '''pygame.draw.rect(WIN, BLACK, BORDER) #draw rect in the WINdow; COLOR; what we draw(somewhere defined rect)'''
    choose = pygame.font.SysFont("calibri", 55).render("PLEASE CHOOSE THE PLAYER:", 1, BLACK)
    option1 = FONT.render("Player 1", 1, BLACK)
    option2 = FONT.render("Player 2", 1, BLACK)
    WIN.blit(choose, (150, 130))
    WIN.blit(option1, (200, 200))
    WIN.blit(option2, (200, 250))
    
    WIN.blit(POINTER, (pointer_rect.x, pointer_rect.y))

    pygame.display.update() #update is needed every time when something is changing

def move_arrow(keys_pressed, pointer_rect):
    if keys_pressed[pygame.K_UP]: #UP move
        pointer_rect.y = 200
    if keys_pressed[pygame.K_DOWN]: #DOWN move
        pointer_rect.y = 250



def main():

    pointer_rect = pygame.Rect(200 - 60, 200, POINTER_WIDTH, POINTER_HEIGHT) #drowe rectangle

    clock = pygame.time.Clock() #defining clock to control FPS
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT event is when we press "x" on the popped up window of the game
                run = False     #If change to "True", the game window will be not possible to close
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()

        move_arrow(keys_pressed, pointer_rect)

        draw_window(pointer_rect)


    main() # to start the game again
    
if __name__ == "__main__":
    main()