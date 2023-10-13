import pygame
import sys

# Initialisieren von pygame
pygame.init()

# Bildschirmgröße und Hintergrundfarbe
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = pygame.display.get_surface().get_size()
background_color = (0, 0, 0)  # Schwarz

# Text und Textfarbe
text = "Nacht Ruhe von 22 bis 6 Uhr - Kein Lärm und keine störenden Aktivitäten in dieser Zeit."
text_color = (255, 255, 255)  # Weiß

# Initialisieren des Bildschirms
pygame.display.set_caption("Laufschrift")

# Font und Textgröße
font = pygame.font.Font(None, 75)
text_surface = font.render(text, True, text_color)

# Textposition
text_x = screen_width  # Startposition am rechten Rand
text_y = screen_height // 2 - text_surface.get_height() // 2

# Bewegungsgeschwindigkeit des Texts
text_speed = 2

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hintergrund löschen
    screen.fill(background_color)

    # Text zeichnen
    screen.blit(text_surface, (text_x, text_y))

    # Text nach links bewegen
    text_x -= text_speed

    # Wenn der Text aus dem Bildschirm verschwindet, setze ihn zurück
    if text_x + text_surface.get_width() < 0:
        text_x = screen_width

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
