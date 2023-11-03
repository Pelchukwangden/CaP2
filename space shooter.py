
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
# Calling the game menu function
game_menu()

# Load alien images
alien_image1 = pygame.image.load("C:\\Users\\user\\Desktop\\pygame\\assets\\12b93f80-c7c0-11ea-9335-0ad96c694158.png")
alien_image1 = pygame.transform.scale(alien_image1, (50, 50))

alien_image2 = pygame.image.load("C:\\Users\\user\\Desktop\\pygame\\assets\\16-161814_clipart-floating-silly-alien-with-tentacles-cartoon-alien.png")
alien_image2 = pygame.transform.scale(alien_image2, (50, 50))

# Def the Alien1 class
class Alien1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = alien_image1
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height 

    def update(self):
        self.rect.y += 3
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

# Def the Alien2 class
class Alien2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = alien_image2
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height 

    def update(self):
        self.rect.y += 2  # Different speed for type 2 alien
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

# Create groups for different types of aliens
alien_group1 = pygame.sprite.Group()
alien_group2 = pygame.sprite.Group()

# Fun to add Alien1 to the group
def add_alien1():
    alien = Alien1()
    alien_group1.add(alien)

# Fun to add Alien2 to the group
def add_alien2():
    alien = Alien2()
    alien_group2.add(alien)
    

# Initialize frame count, rocket speed, and alien spawn timer
frame_count = 0
rocket_speed = 10
alien_spawn_timer = 0
alien_spawn_interval = 50
rocket_alive = True

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check if the rocket is alive
    if rocket_alive:
        # keys pressed by the player
        keys = pygame.key.get_pressed()
        
        # Updating the position of the rocket based on key input
        if keys[pygame.K_LEFT] and rocket.rect.left > 0:  # Check if left key is pressed and rocket is within left boundary
            rocket.rect.x -= rocket_speed
        if keys[pygame.K_RIGHT] and rocket.rect.right < SCREEN_WIDTH:  # Check if right key is pressed and rocket is within right boundary
            rocket.rect.x += rocket_speed

        # Check if the player pressed the spacebar to shoot
        if keys[pygame.K_SPACE]:
            rocket.shoot()

        # Update the position of bullets and check for collisions with aliens
        for bullet in shot_group:
            hit_list1 = pygame.sprite.spritecollide(bullet, alien_group1, True)
            hit_list2 = pygame.sprite.spritecollide(bullet, alien_group2, True)

            if hit_list1:
                bullet.kill()
                score += 1
                score_text = font.render("Score: " + str(score), True, WHITE)
            if hit_list2:
                bullet.kill()
                score += 1
                score_text = font.render("Score: " + str(score), True, WHITE)

        # Check for collisions between the rocket and aliens
        if pygame.sprite.spritecollideany(rocket, alien_group1):
            rocket_alive = False
        if pygame.sprite.spritecollideany(rocket, alien_group2):
            rocket_alive = False

        # Clear the screen and draw background
        screen.blit(background, (0, 0))
        
        # Draw the rocket
        screen.blit(rocket.image, rocket.rect)

        # Updating and drawing Alien1 group
        alien_group1.update()
        alien_group1.draw(screen)

        # Updating and drawing Alien2 group
        alien_group2.update()
        alien_group2.draw(screen)

        # Updating and drawing Bullet group
        shot_group.update()
        for bullet in shot_group:
            if bullet.rect.bottom < 0:
                bullet.kill()
        shot_group.draw(screen)

        # alien spawn timer
        alien_spawn_timer += 0.5

        # If enough time has passed, add new aliens
        if alien_spawn_timer >= alien_spawn_interval:
            add_alien1()
            add_alien2()  # Adding both types of aliens
            alien_spawn_timer = 0

        # Draw the score text
        screen.blit(score_text, score_rect)  

        # Increment frame count
        frame_count += 1

        # Updating the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)
        
    
    else:
        # If rocket is not alive, show game over screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Clear the screen and draw background
        screen.blit(background, (0, 0))

        # Display game over message
        text_surface = font.render("Game Over", True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(text_surface, text_rect)

        # Display restart and quit options
        restart_text = font.render("Restart (enter)", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(restart_text, restart_rect)

        quit_text = font.render("Quit (Q)", True, WHITE)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(quit_text, quit_rect)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)

        # Check for user input to restart or quit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # If Enter is pressed, restart the game
                    rocket_alive = True
                    score = 0
                    score_text = font.render("Score: " + str(score), True, WHITE)
                    rocket.rect.centerx = SCREEN_WIDTH // 2
                    rocket.rect.bottom = SCREEN_HEIGHT - 10
                    alien_group1.empty()
                    alien_group2.empty()
                    shot_group.empty()
                elif event.key == pygame.K_q:
                    # If Q is pressed, quit the game
                    pygame.quit()
                    sys.exit()