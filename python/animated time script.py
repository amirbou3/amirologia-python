import pygame
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌟 Neon Clock")

# Colors
NEON_BLUE = (0, 255, 255)
SHADOW = (0, 100, 100)
BLACK = (10, 10, 10)

# Load a cool font (optional: use a TTF file if you want custom)
font = pygame.font.SysFont("Arial", 72, bold=True)

# Clock to control updates
clock = pygame.time.Clock()

def draw_neon_text(text, x, y):
    # Shadow layer
    shadow_surface = font.render(text, True, SHADOW)
    screen.blit(shadow_surface, (x + 4, y + 4))

    # Main neon text
    neon_surface = font.render(text, True, NEON_BLUE)
    screen.blit(neon_surface, (x, y))

def main():
    while True:
        screen.fill(BLACK)

        # Get current time
        now = datetime.now().strftime("%I:%M:%S %p")

        # Draw glowing time in center
        text_size = font.size(now)
        x = (WIDTH - text_size[0]) // 2
        y = (HEIGHT - text_size[1]) // 2

        draw_neon_text(now, x, y)

        pygame.display.update()
        clock.tick(1)

        # Exit on close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
