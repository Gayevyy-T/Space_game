import pygame
import os
pygame.font.init() # to show text in different font
pygame.mixer.init() # to initialize sound library

#set width and hight of the window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))#window size
pygame.display.set_caption("space_game") #give the name of the popped up window 

WHITE = (255, 255, 255) #set the color (white has these param)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Gun+Silencer.mp3"))

HEALTH_FONT = pygame.font.SysFont("comicsant", 40) # comicsant - type of text/font; 40 -> size
WINNER_FONT = pygame.font.SysFont("comicsant", 100)

FPS = 60 #define framerate per second
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 #size of the ship
VEL = 5 #velocity of the ship
BULLET_VEL = 7 #bullets velocity
MAX_BULLETS = 3

#Since a game is for 2 users, we create 2 userevens that we can call later. If we have the same "+1", it'd be the same event
# the number represent the event - it's unique event ID.
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#defining yellow ship
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
'''YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)) #resize ship to 55 width and 40 height
YELLOW = pygame.transform.rotate(YELLOW_SPACESHIP ,90) #rotate the image to 90%'''
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90) #resize and rotate to 90%

#defining red ship
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)#resize and rotate to 270%

#defining background
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    # WIN.fill(WHITE) #fill the popped up window to white
    WIN.blit(SPACE, (0, 0)) #pasting the space immage to the game
    pygame.draw.rect(WIN, BLACK, BORDER) #draw rect in the WINdow; COLOR; what we draw(somewhere defined rect)
    # to draw the health result:
    red_health_text = HEALTH_FONT.render("HEALTH: " + str(red_health), 1, WHITE) #one is arg and is always 1
    yellow_health_text = HEALTH_FONT.render("HEALTH: " + str(yellow_health), 1, WHITE) #one is arg and is always 1
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    ### '''WIN.blit(YELLOW_SPACESHIP, (300,100)) #blit - to display immage on the screen,(define posiiton(start from top left corner))  "300 -> right & 100 down"'''
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #yellow.x & .y --> take arguments from vars in main -> yellow (100 & 300)
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)    

    pygame.display.update() #update is needed every time when something is changing

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #LEFT move & not allow cross the border
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #RIGHT move
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #UP move
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: #DOWN move (-15 optionally in order not to cross the border)
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #LEFT move
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #RIGHT move
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #UP move
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #DOWN move
        red.y += VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):  #collidrect check if yellow rectangle make collision with the bullet rect
            pygame.event.post(pygame.event.Event(RED_HIT))#we post the event(that was created abowe) that the red was hit
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2)) # give us the exact middle of the WIN
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #drowe rectangle
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock() #defining clock to control FPS
    run = True
    while run:
        clock.tick(FPS) #the loop will run FPS(60) times per sec, not fuster
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT event is when we press "x" on the popped up window of the game
                run = False     #If change to "True", the game window will be not possible to close
                pygame.quit()
###################SHOOTING THE BOOLETS######################
            if event.type == pygame.KEYDOWN: #KEYDOWN means that it react only once when the key is hold down
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)#put the bullet in the middle x position; bullet go from the middle of the character; bullet width(10); bullet height(5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)#put the bullet in the middle x position; bullet go from the middle of the character; bullet width(10); bullet height(5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
###################LOOSER VS WINNER######################
            if event.type == RED_HIT: #created RED_HIT event now exist in the "pygame.event.get()"
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            draw_winner(winner_text) #call the func which pause the text for a few sec
            break
        

        print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed() #call function that press the buttons
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets,  yellow_bullets, red_health, yellow_health)
 

    # pygame.quit() #to quit the game when someonr won
    main() # to start the game again

if __name__ == "__main__":
    main()