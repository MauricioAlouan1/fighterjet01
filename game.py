import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fighter Jet Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
jet_img = pygame.image.load("fighter_jet.png")
missile_img = pygame.image.load("missile.png")

# Scale images
jet_img = pygame.transform.scale(jet_img, (50, 50))
missile_img = pygame.transform.scale(missile_img, (20, 40))

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = jet_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Missile class
class Missile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = missile_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 7

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = -self.rect.height

# Group for all sprites
all_sprites = pygame.sprite.Group()
missiles = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create missiles
for _ in range(10):
    missile = Missile()
    all_sprites.add(missile)
    missiles.add(missile)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollideany(player, missiles):
        running = False
        print("Game Over")

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
