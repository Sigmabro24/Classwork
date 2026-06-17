from itertools import count
from operator import truediv
from os import wait

import pygame
import sys

from pygame.sprite import collide_rect

screen_width = 640
screen_height = 480

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
white =(255,255,255)
screen.fill(white)
rect_x = 10
rect_y = 440
x_speed = 20
y_speed = rect_y-2
speed = 3
rect_width =20
rect_height = 20
floor_x = 0
floor_y = 470
ceiling_x = 0
ceiling_y = 0
right_wall_x = 630
right_wall_y = 10
right_wall_width =10
right_wall_height = 480
left_wall_x = 0
left_wall_y = 10
left_wall_width =10
left_wall_height = 480
floor_width =670
floor_height =10
ceiling_width =670
ceiling_height =10
rect_color=(155,155,155)
player = pygame.Rect(rect_x,rect_y,rect_width,rect_height)
floor = pygame.Rect(floor_x, floor_y, floor_width, floor_height)
right_wall = pygame.Rect(right_wall_x, right_wall_y, right_wall_width, right_wall_height)
ceiling = pygame.Rect(ceiling_x, ceiling_y, ceiling_width, ceiling_height)
left_wall = pygame.Rect(left_wall_x, left_wall_y, left_wall_width, left_wall_height)
running = True


clock = pygame.time.Clock()
FPS = 30
start_count=False
count_jump = 0
start_position = 0

if player.colliderect(floor):
    print("collide")
maze_size = 30
maze=[
    (1,2),
    (3,4),
    (5,6),
    (7,8),
]
def maze_maker(maze_list):  # creates function named maze_maker
    maze_size = 50
    for i in maze:  # creates loop that for every index
        rect3 = pygame.Rect((i[0] * maze_size, i[1] * maze_size, maze_size,
                             maze_size))  # creates rect3 and making it so every individual instance in the list will be multiplied by maze size
        pygame.draw.rect(screen, rect_color, rect3)  # draws the screen, rect2 and rect 3
        if player.colliderect(rect3):
            player.x = rect3.x - rect_width
        if player.colliderect(rect3):
            player.x = rect_width - rect3.x








def main():
    #main game loop
    running = True
    global start_count, count_jump, start_position
    while running:
        clock.tick(FPS)
        ## listen for player events section
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            start_count=True
            start_position=player.y
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += speed
        if (keys[pygame.K_LEFT] or keys[pygame.K_a])and not player.colliderect(floor):
            player.x -= speed
            # if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            #     player.x -= x_speed
            # if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            #     player.x += x_speed
            # if keys[pygame.K_UP] or keys[pygame.K_w]:
            #     player.y -= y_speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not player.colliderect(floor):
            player.y = player.y + rect_height
        if player.colliderect(floor):

                print("collide")
                # if event.key == pygame.K_SPACE:


                # if event.key == pygame.K_SPACE:
                #     start_count=True
                #     start_position=player.y
                # if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                #     player.x = player.x + rect_width
                # if event.key == pygame.K_LEFT:
                #     player.x = player.x - rect_width

        if start_count and count_jump<10 :
            player.y = player.y - 5
            count_jump = count_jump + 1
        elif start_count and start_position > player.y:
            player.y = player .y+ 50
        else:
            count_jump=0
            start_count=False
        screen.fill(white)
        # print(player.y)
        pygame.draw.rect(screen,rect_color,player)
        if player.colliderect(right_wall):
            player.x = right_wall_x - rect_width
            print("collision")
        if player.colliderect(left_wall):
            player.x = rect_width - left_wall_width
            print("collision")
        if player.colliderect(ceiling):
            player.y = rect_height - ceiling_height
        if player.colliderect(floor):
            player.y= floor.y - rect_height




        pygame.draw.rect(screen, rect_color, floor)
        pygame.draw.rect(screen, rect_color, right_wall)
        pygame.draw.rect(screen, rect_color, ceiling)
        pygame.draw.rect(screen, rect_color, left_wall)
        maze_maker(maze)
        pygame.display.flip()






if __name__ == '__main__':
    main()
