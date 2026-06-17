import pygame #imports pygame from library
import sys #imports sys from library
import random

screen_width = 640 #screen's width
screen_height = 480 #screen's height

pygame.init() #starts pygame
screen = pygame.display.set_mode((screen_width, screen_height)) # set the screen width and height on screen
white = (255, 255, 255) # variable that holds a tuple that is rgb and shows the color white
screen.fill(white) #fills the screen with the color white
running = True #sets running to True


clock = pygame.time.Clock()
FPS = 12 #sets the frames per second to 12

rect_x=screen_width/2 #sets the rectangle's x position
rect_y=screen_height/2 #sets the rectangle's y position to the absolute middle
rect_width=5 #sets the rectangles width to 5 pixels
rect_height=5 #sets the rectangles height to 5 pixels
rect_color1 = (120, 120, 60) #sets a color for rectangle 1
rect_color2 = (60, 120, 200) #sets a color for rectangle 2
rect_color = rect_color1 #sets rect_color to rect_color1
rect2_x=screen_width/5 #sets the position of rect2 x
rect2_y=screen_height/2 #sets the position of rect2 y
rect2_width=20 #sets rectangle width to 20
rect2_height=20 #sers rectangle height to 20


rect = pygame.Rect((rect_x, rect_y, rect_width, rect_height)) #creates rect variable with its position and width and height
pygame.draw.rect(screen, rect_color, rect) #draws rect
rect2 = pygame.Rect((rect2_x, rect2_y, rect2_width, rect2_height)) #creates rect2 variable with its position and width and height
pygame.draw.rect(screen, rect_color2, rect2) #draws rect2

maze_size = 30 #variable with 30 pixels assigned to it
maze =[



]
line_list=[]

for x in range(0,640,2):
    y = 240
    line_list.append((x,y))

for box in line_list:
    boxa = pygame.Rect(box[0], box[1],2,2)
    pygame.draw.rect(screen,(128,128,128),boxa)

for y in range(0,480,2):
    x = 320
    line_list.append((x,y))

for box1 in line_list:
    boxb = pygame.Rect(box1[0], box1[1],2,2)
    pygame.draw.rect(screen,(128,128,128),boxb)


def maze_maker(maze_list): #creates function named maze_maker
        maze_size = 30
        for i in maze: #creates loop that for every index
            rect3 = pygame.Rect(( i[0] * maze_size, i[1] * maze_size, maze_size, maze_size)) #creates rect3 and making it so every individual instance in the list will be multiplied by maze size
            pygame.draw.rect(screen, rect_color2, rect3) #draws the screen, rect2 and rect 3


pygame.display.flip()

def main():
    while running: #checks for running to be true
        clock.tick(FPS) #limits frames per second to 30
        for event in pygame.event.get(): #gets things from pygame event
            if event.type == pygame.QUIT: #when you press quit
                pygame.quit() #the game will close
                sys.exit() #it will exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN: #checks if the down arrow is being pressed
                    rect.y = rect.y + rect_height # moves the player down
                if event.key == pygame.K_UP: #checks if the up arrow is being pressed
                    rect.y = rect.y - rect_height #moves player up
                if event.key == pygame.K_LEFT: #checks if left key is being pressed
                    rect.x = rect.x - rect_width #moves the player to the left
                if event.key == pygame.K_RIGHT: #checks if the right key is being pressed
                    rect.x = rect.x + rect_width #moves the player to the right
        screen.fill(white)
        for box in line_list:
            boxa = pygame.Rect(box[0], box[1], 2, 2)
            pygame.draw.rect(screen, (128, 128, 128), boxa)

        pygame.display.flip()


if __name__ == '__main__':
    main()