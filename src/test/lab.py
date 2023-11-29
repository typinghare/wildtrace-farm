import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set up the font
font_size = 36
font = pygame.font.Font(None, font_size)

# Set up the text and border colors
text_color = (255, 255, 255)  # White
border_color = (0, 0, 0)  # Black

# Set up the text
text_content = "Hello, Pygame!"
text_surface = font.render(text_content, True, text_color)

# Set up the border
border_thickness = 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the text with a border
    # Draw the border first
    for dx in range(-border_thickness, border_thickness + 1):
        for dy in range(-border_thickness, border_thickness + 1):
            if dx != 0 or dy != 0:
                screen.blit(font.render(text_content, True, border_color), (dx, dy))

    # Draw the main text
    screen.blit(text_surface, (0, 0))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
