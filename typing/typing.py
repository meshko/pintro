import pygame
from random import randrange 
import math
#import coll
pygame.mixer.init()
sound=pygame.mixer.Sound('evil.wav')

#word="python spy"
#"After the death of Han Solo the resistance"
#"cannot protect itseld"
#"against the treacherous First Order ruled"
# "by the evil Kylo Ren.Princess Leia is dead and Rey" 
#"is on the mission to find Luke Skywalker while Finn"
# "recovers from in a coma.In a month Finn sets" 
#"out on a mission to stop the evil Kylo Ren,"
#"who has developed a new lame lightsaber with"
# "a blade that has no end."
#"Ren is especially angry after his failon the NSL"
#".At the deathstar Finn finds out 2 horrible secrets"
#"the first is the fact that Kylo is the cousin"
# "of Rey and the second most terrible one is that the" 
#"Supreme Leader is actually JarJar Binks ! Will Finn"
# "be able to save the resistance and preserve Rey from" 
# "those horrible secrets ?.........."


screen = pygame.display.set_mode((800, 600))
pygame.font.init()
font = pygame.font.Font(None, 36)

class Word:
    def __init__(self,text):
        self.text=text
        self.speed=1
        self.color=(0,0,255)
        self.rendertext = font.render(self.text, 1, self.color)
        word_width = self.rendertext.get_size()[0]
        self.textpos = self.rendertext.get_rect(centerx=randrange(word_width/2,800-word_width/2)) # screen.get_width()/2

def get_random_word():
    word_index=randrange(0,len(nouns))
    return Word(nouns[word_index])


running = True
clock = pygame.time.Clock()
    
words=[]
f=open('noun.txt','r')
nouns=f.read().splitlines()
f.close()
new_word_interval=45
current_word=None
count = 0

while running:
    if count %round (new_word_interval)==0:
        words.append(get_random_word())
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key in range(0,256):
            print chr(event.key)
            letter=chr(event.key)
            if current_word is None: 
                for word in words:
                    if word.text[0] == letter:
                        current_word = word
                        break 
            if current_word is not None and current_word.text[0] == letter:
                current_word.text = current_word.text[1:]
                current_word.rendertext = font.render(current_word.text, 1, (255,255,255))
                if len(current_word.text)==0:
                    words.remove(current_word)
                    current_word=None
            else:
                sound.play()


    screen.fill((0,0,0))
    for word in words:
        screen.blit(word.rendertext, word.textpos)
        word.textpos=word.textpos.move(0,1)
    
    pygame.display.flip()
    clock.tick(24)
    count = count+1
    new_word_interval=max(20,new_word_interval-0.01)
