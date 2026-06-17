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
    (0,0), #tuples inside of a list
    (1,0),
    (2,0),
    (3,0),
    (3,1),
    (3,2),
    (3,3),
    (3, 4),
    (3, 5),
    (3, 6),
    (3, 7),
    (3, 8),
    (3, 9),
    [4, 9],
    (5, 9),
    (6, 9),
    (7, 9),
    (8, 9),
    (9, 9),
    (10, 9),
    (11, 9),
    (12, 9),
    (0, 11),
    (1, 11),
    (2, 11),
    (3, 11),
    (4, 11),
    (5, 11),
    (6, 11),
    (7, 11),
    (8, 11),
    (9, 11),
    (10, 11),
    (11, 11),
    (12, 11),
    (13,9),
    (13, 11),
    (13, 12),
    (13,13),
    (13,14),
    (13,15),
    (14, 9),
    (15,9),
    (15,10),
    (15,11),
    (15, 12),
    (15, 13),
    (15, 14),
    (15, 15),


]
def maze_maker(maze_list): #creates function named maze_maker
        maze_size = 30
        for i in maze: #creates loop that for every index
            rect3 = pygame.Rect(( i[0] * maze_size, i[1] * maze_size, maze_size, maze_size)) #creates rect3 and making it so every individual instance in the list will be multiplied by maze size
            pygame.draw.rect(screen, rect_color2, rect3) #draws the screen, rect2 and rect 3

def have_collision():
   a= min(rect_x, rect_y, rect2_x, rect2_y)
   b= max(rect_x, rect_y, rect_width, rect_height)




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
        c #calls the function
        pygame.draw.rect(screen, rect_color, rect)
        pygame.draw.rect(screen, rect_color2, rect2)
        pygame.display.flip()


if __name__ == '__main__':
    main()