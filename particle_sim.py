# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:46:11 2023

@author: lcuev
"""
import pygame
import numpy as np


random = np.random.random
col_background = (10, 10, 40)
col_particles = [(30,160,160),(160,30,160),(160,160,30)]
m = 1.1


def dist(i,j,xs,ys):
    return ((xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2) ** 0.5

def dv(i,xs,ys):
    ddx = 0
    ddy = 0
    
    for j in range(3):
        if i != j:
            ddx += (xs[i] - xs[j]) / dist(i,j,xs,ys) ** 3
            ddy += (ys[i] - ys[j]) / dist(i,j,xs,ys) ** 3
    
    ddx *= -2 * m
    ddy *= -2 * m
    
    return ddx,ddy

def potential(x,y,xs,ys):
    pot = [0,0,0]
    
    for i in range(3):
        r = ((x - xs[i])**2 + (y - ys[i]) ** 2) ** 0.5
        pot[i] += 20 * m / r
        if pot[i] > 255/2:
            pot[i] = 255/2

            
    
   
    
        
    return pot



def update(surface,step_size,xs,ys,dxs,dys,dimx,dimy):
    span = 10
    
    for X in range(dimx):
        for Y in range(dimy):
            x =  span * (X / dimx - 0.5)
            y = span * (Y / dimy - 0.5)
            
            r,g,b = potential(x,y,xs,ys)
            col = (g + b,r + b,r + g)
            pygame.draw.rect(surface, col, (X, Y, 1, 1))
    
    for i in range(3):
        x = xs[i]
        y = ys[i]
        
        X = int((x + span/2) * dimx / span)
        Y = int((y + span/2) * dimy / span)
        
        ddx, ddy = dv(i,xs,ys)
        xs[i] += step_size * dxs[i]
        ys[i] += step_size * dys[i]
        dxs[i] += step_size * ddx
        dys[i] += step_size * ddy
        
        if 0 < X < dimx and 0 < Y < dimy:
            pygame.draw.rect(surface, col_particles[i], (X, Y, 2, 2))
            
    
        
    return xs,ys,dxs,dys


def main(dimx, dimy):
    speed = 0.95
    pygame.init()
    surface = pygame.display.set_mode((dimx, dimy))
    pygame.display.set_caption("Particle Simulator")
    sim_length = 10
    step_count = 100
    step_size = sim_length / step_count
    xs = [-1,0,1]
    ys = [-3**0.5/2,3**0.5/2,-3**0.5/2]
    mag = (speed ** 2 + (1.73 * speed) ** 2)**0.5
    dxs = [speed * speed/mag,-speed,speed * speed/mag]
    dys = [-speed * speed*1.73/mag,0,speed* speed*1.73/mag]
    play = True
    n = 0
    
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
               
                # checking if key "A" was pressed
                if event.key == pygame.K_SPACE:
                    play = not play
         

        surface.fill(col_background)
        if play:
            xs,ys,dxs,dys = update(surface,step_size,xs,ys,dxs,dys,dimx,dimy)

            
        pygame.display.update()
        n += 1

if __name__ == "__main__":
    main(150, 150)