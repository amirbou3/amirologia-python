import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario Style Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)  # Light blue sky color
GROUND_COLOR = (139, 69, 19)  # Ground color (brown)

# Character settings
char_width, char_height = 50, 70
char_x, char_y = 100, HEIGHT - char_height - 10
char_speed = 5
gravity = 0.5
jump_power = -10  # Initial jump power
velocity_y = 0
is_jumping = False

# Obstacle settings
obstacle_width, obstacle_height = 40, 60
obstacle_speed = 5  # Start speed
obstacles = []
spawn_timer = 0  # Timer for spawning obstacles

# Score settings
score = 0
high_score = 0
font = pygame.font.Font(None, 36)

# Button settings
button_width, button_height = 150, 50
play_button_x, play_button_y = (WIDTH - button_width) // 2, HEIGHT // 3
restart_button_x, restart_button_y = (WIDTH - button_width) // 2, HEIGHT // 2

# Game state
running = True
game_over = False
game_started = False  # Check if the game has started

# Game loop
while running:
    pygame.time.delay(30)  # Control game speed

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Check if the Play button is clicked
            if not game_started and play_button_x <= mouse_x <= play_button_x + button_width and play_button_y <= mouse_y <= play_button_y + button_height:
                game_started = True  # Start the game
            # Check if the Restart button is clicked
            elif game_over and restart_button_x <= mouse_x <= restart_button_x + button_width and restart_button_y <= mouse_y <= restart_button_y + button_height:
                # Restart the game
                char_x, char_y = 100, HEIGHT - char_height - 10
                obstacles.clear()
                score = 0
                obstacle_speed = 5  # Reset speed
                jump_power = -10  # Reset jump power to initial value
                game_over = False
                game_started = True  # Start the game after restart

    if game_started:
        # Get key states
        keys = pygame.key.get_pressed()

        # Jumping logic
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
            velocity_y = jump_power  # Jump force

        # Apply gravity
        char_y += velocity_y
        velocity_y += gravity

        # Stop falling at ground level
        if char_y >= HEIGHT - char_height - 10:
            char_y = HEIGHT - char_height - 10
            is_jumping = False

        # Increase obstacle speed every 100 points
        obstacle_speed = 5 + (score // 100)  # Speed increases every 100 points

        # At score 1000, increase difficulty by making obstacles taller and moving the character and obstacles higher
        if score >= 1000:
            obstacle_speed = 10  # Increase speed of obstacles even more
            jump_power = -12  # Character jumps higher

        # Spawn obstacles
        spawn_timer += 1
        if spawn_timer > 50:  # Spawn every 50 frames
            spawn_timer = 0
            # Spawn obstacles just above the ground
            obstacle_y = HEIGHT - obstacle_height - 10  # Ground level
            obstacles.append(pygame.Rect(WIDTH, obstacle_y, obstacle_width, obstacle_height))

        # Move obstacles
        for obs in obstacles:
            obs.x -= obstacle_speed

        # Increase obstacle height after score 1000, but ensure they stay above ground level
        if score >= 1000:
            for obs in obstacles:
                # Make sure obstacle height does not push them below the ground
                obs.height = random.randint(80, 120)
                obs.y = HEIGHT - obs.height - 10  # Adjust y to ensure obstacles stay on the ground

        # Remove off-screen obstacles
        obstacles = [obs for obs in obstacles if obs.x > -obstacle_width]

        # Check for collision
        for obs in obstacles:
            if pygame.Rect(char_x, char_y, char_width, char_height).colliderect(obs):
                game_over = True
                if score > high_score:
                    high_score = score  # Update high score

        # Increase score
        score += 1

    # Drawing
    screen.fill(SKY_BLUE)  # Fill the screen with sky blue color

    # Draw ground
    pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - 10, WIDTH, 10))  # Ground line at the bottom

    # Draw obstacles
    for obs in obstacles:
        pygame.draw.rect(screen, BLUE, obs)

    # Draw character if not game over
    if not game_over:
        pygame.draw.rect(screen, RED, (char_x, char_y, char_width, char_height))
    else:
        # Draw restart button
        pygame.draw.rect(screen, BLACK, (restart_button_x, restart_button_y, button_width, button_height))
        text = font.render("Restart", True, WHITE)
        screen.blit(text, (restart_button_x + 40, restart_button_y + 10))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Draw high score
    high_score_text = font.render(f"High Score: {high_score}", True, BLACK)
    screen.blit(high_score_text, (WIDTH - 200, 10))

    # If the game hasn't started yet, show the Play button
    if not game_started:
        # Draw play button
        pygame.draw.rect(screen, BLACK, (play_button_x, play_button_y, button_width, button_height))
        play_text = font.render("Play", True, WHITE)
        screen.blit(play_text, (play_button_x + 50, play_button_y + 10))

    pygame.display.update()

pygame.quit()
