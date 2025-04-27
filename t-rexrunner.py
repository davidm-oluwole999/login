
import pygame
import random
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-Rex Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_COLOR = (200, 200, 200)

# Sprites
try:
    obstacle_image = pygame.image.load(os.path.join('images', 'spikes.jpg'))
    obstacle_image = pygame.transform.scale(obstacle_image, (50, 50))  # Scale image to match obstacle size
except FileNotFoundError:
    print("Error: 'spikes.jpg' not found in the 'images' folder.")
    pygame.quit()
    exit()

# Clock for FPS control
clock = pygame.time.Clock()
FPS = 30

# Font
font = pygame.font.Font(None, 36)


def game_loop():
    # Game variables
    gravity = 1
    jump_power = -15
    t_rex_y = 300
    t_rex_vel_y = 0
    is_jumping = False

    obstacle_x = WIDTH
    obstacle_y = 300
    obstacle_speed = 10

    score = 0

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping and not game_over:
                    t_rex_vel_y = jump_power
                    is_jumping = True
                if event.key == pygame.K_r and game_over:  # Restart key
                    return True  # Restart the game

        if not game_over:
            # Game logic
            t_rex_vel_y += gravity
            t_rex_y += t_rex_vel_y

            if t_rex_y >= 300:  # Ground collision
                t_rex_y = 300
                is_jumping = False

            obstacle_x -= obstacle_speed
            if obstacle_x < -50:  # Reset obstacle
                obstacle_x = WIDTH
                score += 1

            # Collision detection
            t_rex_rect = pygame.Rect(50, t_rex_y, 50, 50)
            obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, 50, 50)
            if t_rex_rect.colliderect(obstacle_rect):
                game_over = True

        # Drawing
        screen.fill(WHITE)  # Background
        pygame.draw.rect(screen, BLACK, pygame.Rect(50, t_rex_y, 50, 50))  # T-Rex
        screen.blit(obstacle_image, (obstacle_x, obstacle_y))  # Obstacle image
        pygame.draw.rect(screen, GROUND_COLOR, (0, 350, WIDTH, 50))  # Ground

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = font.render("Game Over! Press 'R' to Restart", True, BLACK)
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))

        pygame.display.flip()  # Update display
        clock.tick(FPS)

    return False  # Exit the game


# Main game loop
while game_loop():
    pass

pygame.quit()