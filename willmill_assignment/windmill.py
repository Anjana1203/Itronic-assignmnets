import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Set the width and height of the window
width, height = 400, 600
line_color = (50, 50, 50)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wind Turbine")

# Load the turbine image
turbine_image = pygame.image.load("turbine.png")

# Define the turbine position and rotation angle
turbine_pos = (width // 2, height // 2)
turbine_angle = 0

def rotate_image(image, angle):
    '''Method to rotate an image
    
    Args:
        image (pygame image): The image want to rotate
        angle (int): Angle to rotate

    Returns:
        rotated image
        image react object
    '''
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect().center)
    return rotated_image, new_rect

def read_speed_setting():
    '''Method to read the speed settings from a file

    Returns:
        speed of rotatation as int
    '''
    with open("settings.txt", "r") as file:
        speed = int(file.readline())
        return max(1, min(speed, 10))

running = True
while running:
    if pygame.time.get_ticks() % 10000 < 5000:
        speed = read_speed_setting()

    screen.fill((255, 255, 255))

    # draw the turbine-leg
    pygame.draw.rect(screen, line_color, pygame.Rect(178, 190, 10, 380))
    
    # Rotate and draw the turbine leaf image
    rotated_turbine, turbine_rect = rotate_image(turbine_image, turbine_angle)
    screen.blit(rotated_turbine, turbine_rect)
    pygame.display.flip()

    # Update the rotation angle based on the speed
    turbine_angle += speed

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

    # Delay to control the frame rate
    pygame.time.delay(10)

# Quit the game
pygame.quit()
