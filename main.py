from kramer import kramer
import pygame
from time import sleep
from playsound import playsound

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()
cosmo = kramer()

# Set the dimensions of the display
width, height = 960, 720
screen = pygame.display.set_mode((width, height))
fps = 120

# Load the JPG image
markov_map = pygame.image.load("images/kramer_markov.jpg")
moving_cosmo = pygame.image.load("images/cosmo.png")
moving_cosmo = pygame.transform.scale(moving_cosmo, (moving_cosmo.get_width() // 10, moving_cosmo.get_height() // 10))
matrix = pygame.image.load("images/matrix.png")
matrix = pygame.transform.scale(matrix, (matrix.get_width() // 4, matrix.get_height() // 4))

times = pygame.font.match_font("Times", bold = False)
courier_bold = pygame.font.match_font("Courier", bold = True)
font = pygame.font.Font(times, 24)
font_bold = pygame.font.Font(courier_bold, 24)

def print_top():
    temp = 5
    text = ["Kramers going from ", cosmo.at_apt, " apartment to ", cosmo.dest_apt, " apartment (P = ", str(cosmo.chance), ")"]
    
    for i in range(len(text)):
        if not i % 2:
            snippet = font.render(text[i], True, (0,0,0))
            screen.blit(snippet, (temp,5))
            temp += snippet.get_width()
        else:
            snippet = font_bold.render(text[i], True, (0,0,0))
            screen.blit(snippet, (temp,5))
            temp += snippet.get_width()

cosmo.run()
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    cosmo.on_the_move()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Blit the image onto the screen
    screen.blit(pygame.image.load("images/" + cosmo.image), (0, 0))

    screen.blit(matrix, (740, 600))

    screen.blit(moving_cosmo, cosmo.pixel_loc)

    print_top()

    if cosmo.change_img_flag:
        img = pygame.image.load("images/" + f'{cosmo.kramer_loc}.png').convert_alpha() # f'{cosmo.kramer_loc}{cosmo.kramer_loc_old}
        img = pygame.transform.scale(img, (width, height))
        img.set_alpha(220)
        screen.blit(img, (0, 0))
        print_top()
        pygame.display.flip()
        playsound(f'audio_files/{cosmo.kramer_loc_old}{cosmo.kramer_loc}.m4a')
        cosmo.change_img_flag = 0
        cosmo.run()

    clock.tick(fps)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()