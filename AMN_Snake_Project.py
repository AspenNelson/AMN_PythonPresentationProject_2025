# Name: Aspen Nelson
# Instructor: 
# Date:12/09/2025
# Description: 

# imports
import pygame, sys, random
from pygame.math import Vector2

# class for Snake
class SNAKE:
    def __init__(self):
        # initial snake body
        self.snake_body = [Vector2(5,10), Vector2 (4,10), Vector2(3,10)]
        # initialize snake direction
        self.direction = Vector2(0,0)
        # initialize snake growth as False
        self.growth = False
        
        # import graphics for different parts of the snake
        # head
        self.head_up = pygame.image.load('head_up.png').convert_alpha()
        self.head_down = pygame.image.load('head_down.png').convert_alpha()
        self.head_right = pygame.image.load('head_right.png').convert_alpha()
        self.head_left = pygame.image.load('head_left.png').convert_alpha()
        
        # tail
        self.tail_up = pygame.image.load('tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('tail_left.png').convert_alpha()
        
        # body
        self.body_vertical = pygame.image.load('body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('body_horizontal.png').convert_alpha()
        self.body_topright = pygame.image.load('body_topright.png').convert_alpha()
        self.body_topleft = pygame.image.load('body_topleft.png').convert_alpha()
        self.body_bottomright = pygame.image.load('body_bottomright.png').convert_alpha()
        self.body_bottomleft = pygame.image.load('body_bottomleft.png').convert_alpha()
        
    # draw the snake
    def draw_snake(self):
        # checks what direcrtion head is facing
        self.head_direction()
        self.tail_direction()
        
        # utilize snake graphics and draw the snake
        for  index,block in enumerate(self.snake_body):
            # use rect for position
            x_pos = int(block.x * c_size)
            y_pos = int(block.y * c_size)
            block_rect = pygame.Rect(x_pos, y_pos, c_size, c_size)
            
            # update head graphics
            if index == 0:
                screen.blit(self.head, block_rect)
            # update tail graphics
            elif index == len(self.snake_body) - 1:
                screen.blit(self.tail, block_rect)
            #update body grpahics
            else: 
                pre_block = self.snake_body[index + 1] - block
                nxt_block = self.snake_body[index - 1] - block
                # if horizontal or vertical body
                if pre_block.x == nxt_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif pre_block.y == nxt_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                # curved body
                else:
                    if pre_block.x == -1 and nxt_block.y == -1 or pre_block.y == -1 and nxt_block.x == -1:
                        screen.blit(self.body_topleft, block_rect)
                    elif pre_block.x == -1 and nxt_block.y == 1 or pre_block.y == 1 and nxt_block.x == -1:
                        screen.blit(self.body_bottomleft, block_rect)
                    elif pre_block.x == 1 and nxt_block.y == -1 or pre_block.y == -1 and nxt_block.x == 1:
                        screen.blit(self.body_topright, block_rect)
                    elif pre_block.x == 1 and nxt_block.y == 1 or pre_block.y == 1 and nxt_block.x == 1:
                        screen.blit(self.body_bottomright, block_rect)
                
    
             
    # checks for direction of the head of the snake and assigns graphics            
    def head_direction(self):
        head_pos = self.snake_body[1] - self.snake_body[0]
        if head_pos == Vector2(1,0):
            self.head = self.head_left
        elif head_pos == Vector2(-1,0):
            self.head = self.head_right
        elif head_pos == Vector2(0,1):
            self.head = self.head_up
        elif head_pos == Vector2(0,-1):
            self.head = self.head_down
      
    # checks for direction of tail and assigns graphics      
    def tail_direction(self):
        tail_pos = self.snake_body[-2] - self.snake_body[-1]
        if tail_pos == Vector2(1,0):
            self.tail = self.tail_left
        elif tail_pos == Vector2(-1,0):
            self.tail = self.tail_right
        elif tail_pos == Vector2(0,1):
            self.tail = self.tail_up
        elif tail_pos == Vector2(0,-1):
            self.tail = self.tail_down

    # move snake
    def move_snake(self):
        # allows snake to grow
        if self.growth == True:
            # make a copy of the snake body
            body_copy = self.snake_body[:]
            # moves snake with player input
            body_copy.insert(0, body_copy[0] + self.direction)
            self.snake_body = body_copy[:]
            self.growth = False
        else:    
            # make a copy of the snake body
            body_copy = self.snake_body[:-1]
            # moves snake with player input
            body_copy.insert(0, body_copy[0] + self.direction)
            self.snake_body = body_copy[:]
    
    # lengthens snake
    def grow_snake(self):
        self.growth = True
        
    # resets snake if game fails
    def reset_snake(self):
        self.snake_body = [Vector2(5,10), Vector2 (4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        
        

# Class for apples snake eats
class APPLE:
    def __init__(self):
        # calls move_random
        self.move_random()
        
        # import apple graphic
        self.apple_image = pygame.image.load('apple.png').convert_alpha()

        
    def draw_apple(self):
        # Create the apple rect
        apple_rect = pygame.Rect(self.pos.x * c_size ,self.pos.y * c_size ,c_size,c_size)
        # Use apple graphic
        screen.blit(self.apple_image, apple_rect)
        
    def move_random(self):
        # x and y positons of apple
        # use random to make sure the apple appears at random
        self.x = random.randint(0, c_num - 1)
        self.y = random.randint(0, c_num - 1)
        # put values into vector
        self.pos = Vector2(self.x , self.y)

# Main Class
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.apple = APPLE()
        
    # updates the snake    
    def update(self):
        self.snake.move_snake()
        self.eat_apple()
        self.collision()
       
    # draws the elements in the game 
    def draw_game(self):
        self.apple.draw_apple()
        self.snake.draw_snake()
        self.score_display()
        
    # checks if snake eats the apple
    def eat_apple(self):
        if self.apple.pos == self.snake.snake_body[0]:
            # move apple
            self.apple.move_random()
            # lengthen snake
            self.snake.grow_snake()
        
        #make sure apple does not spawn in snake
        for block in self.snake.snake_body[1:]:
            if block == self.apple.pos:
                self.apple.move_random()
                
    # Check if snake hits itself or wall
    def collision(self):
        # if snake hits walls
        if not 0 <= self.snake.snake_body[0].x < c_num or not 0 <= self.snake.snake_body[0].y < c_num:
            self.game_over()
        # if snake hits itself
        for block in self.snake.snake_body[1:]:
            if block == self.snake.snake_body[0]:
                self.game_over()
        
    # game is over
    def game_over(self):
        self.snake.reset_snake()
        
    def score_display(self):
        score = str(len(self.snake.snake_body) - 3)
        score_disp = font.render(score, True, (56,74,12))
        score_xpos = int(c_size * c_num - 60)
        score_ypos = int(c_size * c_num - 40)
        score_rect = score_disp.get_rect(center = (score_xpos, score_ypos))
        screen.blit(score_disp, score_rect)
        
        
# start pygame
pygame.init()

# Set up window and background
# Make cell size and number
c_size = 30
c_num = 15
# make screen and clock
screen = pygame.display.set_mode((c_num * c_size, c_num * c_size))
clock = pygame.time.Clock()

#set up pygame text font
font = pygame.font.Font(None, 25)


# Variables to create timer for capturing user input every 150ms
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# create main
main_game = MAIN()

# Main Game Loop
while True:
    # Event loop to keep game open
    for event in pygame.event.get():
        # allows player to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # allows player to move snake
        if event.type == SCREEN_UPDATE:
            main_game.update()
        # specifies what to do for user input
        # uses arrow commands
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y !=  1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y !=  -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x !=  -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x !=  1:
                    main_game.snake.direction = Vector2(-1,0)
    
    # fills screen with selected color
    screen.fill((175,215,70))
    
    # draw game elements
    main_game.draw_game()
    
    # updates display for everything added
    pygame.display.update()
    
    # 60 fps
    clock.tick(60)