import pygame
from random import randrange 
import math
pygame.mixer.init()
sound=pygame.mixer.Sound('evil.wav')

pygame.font.init()    
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((800, 600))    

class Word:
    def __init__(self, word):
        self.word = word
        self.rendered_text = font.render(word, 1, (255,255,0))
        halfw = screen.get_width()/2
        self.textpos = self.rendered_text.get_rect(centerx=(halfw + randrange(-halfw,halfw)))
        self.speed = 1

    def remove_letter(self):
        self.word = self.word[1:]
        self.rendered_text = font.render(self.word, 1, (255,255,0))
        return self.word == ''

    def move_down(self):
        self.textpos=self.textpos.move(0, self.speed)
        self.speed *= 1.01

words = [Word("test"), Word("starwars")]

running = True
clock = pygame.time.Clock()

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key in range(0,256):
            #print chr(event.key)
            letter=chr(event.key)
            if words[0].word[0] == letter:
                if words[0].remove_letter():
                    words.remove(words[0])
            else:
                sound.play()
    screen.fill((0,0,0))

    for word in words:
        screen.blit(word.rendered_text, word.textpos)
        word.move_down()
    
    pygame.display.flip()
    clock.tick(24)
