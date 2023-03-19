import pygame 
from pygame import mixer

pygame.init()
mixer.init()
pygame.display.set_caption("Askar's player :)")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 50
done = False
n = 0
musics = ['blindinglights.mp3', 'giant.mp3', 'humility.mp3', 'icantfeelmyface.mp3', 'moveslikejagger.mp3']
plays = ['blindinglights_play.png', 'giant_play.png', 'humility_play.png', 'cantfeelmyface_play.png', 'moveslikejagger_play.png']
pauses = ['blindinglights_pause.png', 'giant_pause.png', 'humility_pause.png', 'cantfeelmyface_pause.png', 'moveslikejagger_pause.png']

def start(n):
    
    # Loading nth audio file into our player
    mixer.music.load(musics[n])
      
    mixer.music.set_volume(0.2)
    # Playing our music
    mixer.music.play()

start(n)
screen.blit(pygame.image.load(plays[n]), (0, 0))
paused = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if(paused == False):
                mixer.music.pause()
                paused = True
                screen.blit(pygame.image.load(pauses[n]), (0, 0))
            else:
                mixer.music.unpause()
                paused = False
                screen.blit(pygame.image.load(plays[n]), (0, 0))
            # b = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if n == 4: n = 0
            else: n += 1
            screen.blit(pygame.image.load(plays[n]), (0, 0))
            start(n)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if n == 0: n = 4
            else: n -= 1
            screen.blit(pygame.image.load(plays[n]), (0, 0))
            start(n)
  
    pygame.display.flip()
    clock.tick(FPS)
# start(0)
pygame.quit()