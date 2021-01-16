
import pygame,random
pygame.init()
# colors 
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

screen_width = 1550
screen_height = 800
game_window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("nirbhay sharma snake ")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None,55)

def screen_score(text ,color , x,y):
    screen_text = font.render(text, True,color)
    game_window.blit(screen_text,[x,y])
def plot_snake(gamewin,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window , color , [x,y,snake_size,snake_size])

def gameloop():
    with open('file.txt') as f:
        highscore = f.read()
    snk_list = []
    snk_length = 1
    game_exit = False 
    game_over = False
    snake_x=screen_width//2
    snake_y=screen_height//2
    snake_size_x = 10
    snake_size = 10
    snake_size_y = 10
    vel_x = 0
    vel_y = 0
    food_x = random.randint(20,screen_width-20)
    food_y = random.randint(20,screen_height-20)
    score = 0

    fps = 30
    while not game_exit:
        if game_over:
            game_window.fill(black)
            screen_score('game over press enter to continue',red,screen_width//2-250,screen_height//2-50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x += 8
                        vel_y = 0
                    elif event.key == pygame.K_DOWN:
                        vel_y += 8
                        vel_x = 0
                    elif event.key == pygame.K_LEFT:
                        vel_x -=8
                        vel_y = 0
                    elif event.key == pygame.K_UP:
                        vel_y -= 8
                        vel_x = 0

            snake_x += vel_x
            snake_y += vel_y
            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score += 10
                food_x = random.randint(20,screen_width-20)
                food_y = random.randint(20,screen_height-20)
                snk_length += 5
                if score>int(highscore):
                    highscore = score
                    with open("file.txt",'w') as f:
                        f.write(f"{highscore}")
            game_window.fill(black)
            screen_score(f'score: {score} highscore: {highscore}',green,5,5)
            pygame.draw.rect(game_window , red , [food_x,food_y,snake_size,snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(game_window,white,snk_list,snake_size)
    
        pygame.display.update() 
        clock.tick(fps)   
    pygame.quit()
    quit()
gameloop()
