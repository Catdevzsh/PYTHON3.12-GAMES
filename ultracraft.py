import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 50

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Minecraft with HUD")

# Block position (player)
player_x, player_y = WIDTH // 2, HEIGHT // 2

# Fonts
title_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)

# HUD values
max_health = 20
max_hunger = 20
health = 20  # Full health
hunger = 20  # Full hunger

# Function to draw the HUD bars
def draw_hud():
    # Health bar
    for i in range(max_health // 2):
        if i < health // 2:
            pygame.draw.rect(screen, RED, (20 + i * 40, 20, 36, 36))
        else:
            pygame.draw.rect(screen, WHITE, (20 + i * 40, 20, 36, 36))
            pygame.draw.rect(screen, BLACK, (20 + i * 40, 20, 36, 36), 2)

    # Hunger bar
    for i in range(max_hunger // 2):
        if i < hunger // 2:
            pygame.draw.rect(screen, YELLOW, (20 + i * 40, 60, 36, 36))
        else:
            pygame.draw.rect(screen, WHITE, (20 + i * 40, 60, 36, 36))
            pygame.draw.rect(screen, BLACK, (20 + i * 40, 60, 36, 36), 2)

# Function to draw the main menu
def draw_main_menu():
    screen.fill(WHITE)
    title_text = title_font.render("MINECRAFT", True, GREEN)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - title_text.get_height() // 2 - 50))
    prompt_text = small_font.render("Press any key to start", True, BLACK)
    screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT // 2 - prompt_text.get_height() // 2 + 50))
    pygame.display.flip()

# Main game loop
in_menu = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and in_menu:
            in_menu = False

    if in_menu:
        draw_main_menu()
    else:
        # Get the keys pressed
        keys = pygame.key.get_pressed()

        # Move the player block
        if keys[pygame.K_LEFT]:
            player_x -= BLOCK_SIZE
        if keys[pygame.K_RIGHT]:
            player_x += BLOCK_SIZE
        if keys[pygame.K_UP]:
            player_y -= BLOCK_SIZE
        if keys[pygame.K_DOWN]:
            player_y += BLOCK_SIZE

        # Ensure the block stays within bounds
        player_x = max(0, min(player_x, WIDTH - BLOCK_SIZE))
        player_y = max(0, min(player_y, HEIGHT - BLOCK_SIZE))

        # Clear the screen
        screen.fill(WHITE)

        # Draw the player block
        pygame.draw.rect(screen, GREEN, (player_x, player_y, BLOCK_SIZE, BLOCK_SIZE))

        # Draw the HUD
        draw_hud()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(30)

# Quit pygame
pygame.quit()
sys.exit()
