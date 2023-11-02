
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space shooting")

# Load the background image
background = pygame.image.load("C:\\Users\\user\\Desktop\\pygame\\assets\\12b93f80-c7c0-11ea-9335-0ad96c694158.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the rocket image
rocket_image = pygame.image.load("C:\\Users\\user\\Desktop\\pygame\\assets\\rocket.png")
rocket_image = pygame.transform.scale(rocket_image, (100, 100))

# Load the bullet image
bullet_image = pygame.image.load("C:\\Users\\user\\Desktop\\pygame\\assets\\UZltYi.png")
bullet_image = pygame.transform.scale(bullet_image, (20, 20))

# Create a group for bullets
shot_group = pygame.sprite.Group()