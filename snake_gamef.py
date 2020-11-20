import pygame
import random
pygame.mixer.init()

pygame.init()

# Colors
white=(255, 255, 255)
red=(255, 0, 0)
black=(0, 0, 0)
blue=(0,0,255)
green=(50,205,50)
pink=(139,10,80)
yellow=(255,193,37)
brown=(139,69,19)

# Creating window
screen_width=1200
screen_height=600
game_window=pygame.display.set_mode((screen_width, screen_height))
# background image
#back_img=pygame.image.load("gdimg.jpeg")
#back_img=pygame.transform.scale(back_img,(screen_width,screen_height)).convert_alpha()
# front image

front_img=pygame.image.load("front.jpeg")
front_img=pygame.transform.scale(front_img,(screen_width,screen_height)).convert_alpha()

#last_img
last_img=pygame.image.load("last.jpeg")
last_img=pygame.transform.scale(last_img,(screen_width,screen_height+100)).convert_alpha()

pygame.display.set_caption("Snake game with suraj")
pygame.display.update()
clock=pygame.time.Clock()

font=pygame.font.SysFont(None, 70)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

def plot_snake(game_window, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        game_window.fill(green)
        game_window.blit(front_img,(0,0))
        text_screen("welcome to snake game",red,280,10)
        text_screen("-made by suraj gupta",red,290,60)
        text_screen("press space bar to play",black,290,100)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load("bck.mp3")
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)                


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 65
    snake_y = 55
    vx = 0
    vy = 0
    snk_list = []
    snk_length = 1

    with open("highscore.txt","r") as f:
        highscore=f.read()
    
     

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_vel= 5
    snake_size = 20
    fps = 60
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
              f.write(str(highscore))
            game_window.fill(white)
            game_window.blit(last_img,(0,0))
            text_screen("Game Over! Press Enter To Continue", red, 170, 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vx = init_vel
                        vy = 0

                    if event.key == pygame.K_LEFT:
                        vx = - init_vel
                        vy = 0

                    if event.key == pygame.K_UP:
                        vy = -init_vel
                        vx = 0

                    if event.key == pygame.K_DOWN:
                        vy = init_vel
                        vx = 0

            snake_x = snake_x + vx
            snake_y = snake_y + vy

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

                if score>int(highscore):
                    highscore=score

            game_window.fill(white)
           # game_window.blit(back_img,(0,0))
            text_screen("Score: " + str(score)+"  " +"highscore: "+str(highscore), blue, 5, 5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()
            plot_snake(game_window, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

