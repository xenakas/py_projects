
# coding: utf-8

# In[1]:


import pygame
import numpy as np

pygame.init()
size = (300, 200)
screen = pygame.display.set_mode(size) 
yellow = pygame.Color('yellow')
blue = pygame.Color('blue')
done = True
fps = 100
clock = pygame.time.Clock()
screen.fill(blue)
k=0
centers = []
direct = []
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            q = list(event.pos)
            w = 10
            centers.append(q)
            direct.append([1,-1])
            k = 1
    pygame.display.flip()
    while k == 1:
        screen.fill(blue)
        for i in range(len(centers)):
            pygame.draw.circle(screen, yellow, centers[i], w)
            if (centers[i][1] == 5) or (centers[i][1] == 200-5) :
                direct[i][1] *= -1
            if (centers[i][0] == 300-5) or (centers[i][0] == 5) :
                direct[i][0] *= -1
            centers[i][0]+=direct[i][0]
            centers[i][1]+=direct[i][1]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    k = 0
                    done = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    q = list(event.pos)
                    centers.append(q)
                    direct.append([1,-1])
                    break                    
        pygame.display.flip()
        clock.tick(fps)
# завершение работы:
pygame.quit()
                

