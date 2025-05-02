import pygame
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🕒 Live Clock")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font setup
font = pygame.font.SysFont("Arial", 60)

# Clock to control frame rate
clock = pygame.time.Clock()

def draw_time():
    now = datetime.now().strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    text_surface = font.render(now, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)

# Main loop
while True:
    screen.fill(BLACK)

    draw_time()

    pygame.display.update()
    clock.tick(1)  # update once per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
