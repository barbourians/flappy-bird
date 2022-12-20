import pygame

# Initialize Pygame
pygame.init()

# Set the window size and title
WIDTH = 400
HEIGHT = 600
TITLE = "Flappy Bird"

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Set the background color
bg_color = (255, 255, 255)

# Create the bird sprite
bird_image = pygame.image.load("bird.png")
bird_rect = bird_image.get_rect()
bird_rect.center = (WIDTH // 2, HEIGHT // 2)

# Set the gravity and lift
gravity = 0.25
lift = -5

# Set the initial velocity
velocity = 0

# Set the pipe width and gap size
pipe_width = 50
pipe_gap = 150

# Create a list to store the pipes
pipes = []

# Set the clock
clock = pygame.time.Clock()

# Set the game running flag
running = True

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle space bar press to lift the bird
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = lift

    # Update the bird's velocity and position
    velocity += gravity
    bird_rect.y += velocity

    # Check for collision with the ground
    if bird_rect.bottom > HEIGHT:
        running = False

    # Check for collision with the pipes
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            running = False

    # Remove pipes that are off the screen
    pipes = [pipe for pipe in pipes if pipe.right > 0]

    # Add a new pipe if needed
    if len(pipes) == 0 or pipes[-1].right < WIDTH - pipe_width:
        y = 0
        gap = pipe_gap
        while y + gap < HEIGHT:
            y += 50
        pipe = pygame.Rect(WIDTH, y, pipe_width, HEIGHT - y - gap)
        pipes.append(pipe)

    # Draw the background
    screen.fill(bg_color)

    # Draw the pipes
    for pipe in pipes:
        pygame.draw.rect(screen, (0, 0, 0), pipe)

    # Draw the bird
    screen.blit(bird_image, bird_rect)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
