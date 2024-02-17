import pygame
import random
import os
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 2 * player_height
player_speed = 5
player_image = pygame.image.load("/home/jake/Downloads/mario2.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (player_width, player_height))

# Obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 6
obstacle_frequency = 10  # Higher values make the game harder
obstacle_image = pygame.image.load("/home/jake/Downloads/enemy1.png").convert_alpha()
obstacle_image = pygame.transform.scale(obstacle_image, (obstacle_width, obstacle_height))

# Background
background_image = pygame.image.load("/home/jake/Downloads/road-texture4.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fun Pygame")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Font for displaying score and timer
font = pygame.font.Font(None, 36)

# Game states
GAME_START = 0
GAME_PLAYING = 1
GAME_MENU = 2
GAME_QUIT = 3

game_state = GAME_START

# Timer variables
start_time = time.time()
elapsed_time = 0

# Function to draw the player
def draw_player(x, y):
    screen.blit(player_image, (x, y))

# Function to draw obstacles
def draw_obstacle(x, y):
    screen.blit(obstacle_image, (x, y))

# Function to display start menu
def display_start_menu():
    screen.fill(BLACK)
    start_text = font.render("Press SPACE to play", True, WHITE)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(start_text, start_rect)

    difficulty_text = font.render("Select Difficulty: 1-Easy, 2-Medium, 3-Hard", True, WHITE)
    difficulty_rect = difficulty_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(difficulty_text, difficulty_rect)

    pygame.display.flip()

# Function to display menu
def display_menu(score):
    screen.fill(BLACK)
    final_score_text = font.render("Final Score: " + str(score), True, WHITE)
    final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(final_score_text, final_score_rect)

    elapsed_time_text = font.render("Time: " + format_time(elapsed_time), True, WHITE)
    elapsed_time_rect = elapsed_time_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(elapsed_time_text, elapsed_time_rect)

    message = "Press ENTER to retry or SPACE to quit"
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Function to display game over screen
def display_game_over(score):
    screen.fill(BLACK)
    game_over_text = font.render("Game Over", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(game_over_text, game_over_rect)

    final_score_text = font.render("Final Score: " + str(score), True, WHITE)
    final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(final_score_text, final_score_rect)

    elapsed_time_text = font.render("Time: " + format_time(elapsed_time), True, WHITE)
    elapsed_time_rect = elapsed_time_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
    screen.blit(elapsed_time_text, elapsed_time_rect)

    message = "Press ENTER to retry or SPACE to quit"
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT * 5 // 6))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Function to format time in HH:MM:SS format
def format_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Main game loop
score = 0
obstacles = []
difficulty = 1  # Default difficulty is easy

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_state == GAME_START:
        display_start_menu()

        if keys[pygame.K_SPACE]:
            game_state = GAME_PLAYING

    elif game_state == GAME_PLAYING:
        player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

        # Spawn obstacles
        if random.randint(1, obstacle_frequency) == 1:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append([obstacle_x, obstacle_y])

        # Move obstacles and check collisions
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if (
                player_x < obstacle[0] + obstacle_width
                and player_x + player_width > obstacle[0]
                and player_y < obstacle[1] + obstacle_height
                and player_y + player_height > obstacle[1]
            ):
                game_state = GAME_MENU

            if obstacle[1] > HEIGHT:
                score += 1
                obstacles.remove(obstacle)

        # Draw background
        screen.blit(background_image, (0, 0))

        # Draw everything
        draw_player(player_x, player_y)
        for obstacle in obstacles:
            draw_obstacle(obstacle[0], obstacle[1])

        # Display the score
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update and display the timer
        elapsed_time = time.time() - start_time
        timer_text = font.render("Time: " + format_time(elapsed_time), True, WHITE)
        timer_rect = timer_text.get_rect(topright=(WIDTH - 10, 10))
        screen.blit(timer_text, timer_rect)

    elif game_state == GAME_MENU:
        display_game_over(score)

        if keys[pygame.K_RETURN]:  # Retry
            game_state = GAME_PLAYING
            player_x = WIDTH // 2 - player_width // 2
            player_y = HEIGHT - 2 * player_height
            obstacles = []
            score = 0
            start_time = time.time()

        elif keys[pygame.K_SPACE]:  # Quit
            game_state = GAME_QUIT

    elif game_state == GAME_QUIT:
        running = False

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()