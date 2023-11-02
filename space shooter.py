
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# def screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space shooting")

# Load the background image
background = pygame.image.load("C:\\Users\\user\\Desktop\\pygame\\assets\\310872-Endless_Space-video_games-space.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the rocket image
rocket_image = pygame.image.load("C:\\Users\\user\\Desktop\\pygame\\assets\\rocket.png")
rocket_image = pygame.transform.scale(rocket_image, (100, 100))

# Load the bullet image
bullet_image = pygame.image.load("C:\\Users\\user\\Desktop\\pygame\\assets\\UZltYi.png")
bullet_image = pygame.transform.scale(bullet_image, (20, 20))

# Create a group for bullets
shot_group = pygame.sprite.Group()

# Def the Rocket class
class Rocket(pygame.sprite.Sprite):
    def __init__(self):  
        super().__init__()
        self.image = rocket_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.cooldown_time = 500  # Cooldown time for shooting in milliseconds
        self.last_shot_time = pygame.time.get_ticks()  # Initialize last shot time

    def shoot(self):
        # Get the current time
        current_time = pygame.time.get_ticks()
        
        # Check if enough time has passed since the last shot
        if current_time - self.last_shot_time > self.cooldown_time:
            # Create a bullet and add it to the shot group
            bullet = Bullet(self.rect.centerx, self.rect.top)
            shot_group.add(bullet)
            self.last_shot_time = current_time  # Update last shot time

# Def the Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):  
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        # Move the bullet upwards
        self.rect.y -= 8  
        
        # Check if the bullet is off-screen, and if so, remove it from the group
        if self.rect.bottom < 0:
            self.kill()

# Create an instance of the Rocket class
rocket = Rocket()

# Load the game font
font = pygame.font.Font(None, 36)

# Initialize the score
score = 0

# Create a text surface for the score
score_text = font.render("Score: " + str(score), True, WHITE)
score_rect = score_text.get_rect(topleft=(10, 10))

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Define a loading screen function
def loading_screen():
    loading_screen_height = 0
    
    # Gradually fill the screen with white
    while loading_screen_height < SCREEN_HEIGHT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        loading_screen_height += 5

        # Clear the screen and draw a white rectangle from the bottom
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (0, SCREEN_HEIGHT - loading_screen_height, SCREEN_WIDTH, loading_screen_height))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)

# Call the loading screen function
loading_screen()

# Define a game menu function and its options
def game_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


        screen.blit(background, (0, 0))

        text_surface = font.render("SPACE SHOOTER", True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(text_surface, text_rect)

        new_game_text = font.render("Start (enter)", True, WHITE)
        new_game_rect = new_game_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(new_game_text, new_game_rect)

        quit_text = font.render("Quit (Q)", True, WHITE)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(quit_text, quit_rect)
        
        pygame.display.flip()

        clock.tick(30)

