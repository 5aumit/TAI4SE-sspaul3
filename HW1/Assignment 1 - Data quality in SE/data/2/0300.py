# basic_flag.py
# christopher mulkey
# 11/05/2012
# lab 1

import pygame

width = 640
height = 480

pygame.init()

screen = pygame.display.set_mode((width, height)) # Screen


#screen.fill(0, 0, 0)            	# Black Background
pygame.Surface.draw.rect(0, 0, 104)     # White Flag Background
pygame.Surface.draw.circle(0, 0, 255)   # Blue
pygame.Surface.draw.circle(255, 255, 0)	# Yellow
pygame.Surface.draw.circle(0, 0, 0)	# Black
pygame.Surface.draw.circle(0, 255, 0)	# Green
pygame.Surface.draw.circle(255, 0, 0)	# Red


running = True
pygame.display.flip()
for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key ==pygame.K_q):
			run = False

####
#import pygame
#
#width = 640
#height = 480
#
#pygame.init()
#
#screen = pygame.display.set_mode((width, height)) # Screen
##
#screen.fill((0, 0, 0))            	  # Black Background
#pygame.draw.rect(screen,(0, 0, 104),(400, 200))   # White Flag Background
#pygame.draw.circle(screen,(0, 0, 255))    # Blue
#pygame.draw.circle(screen, (255, 255, 0)) # Yellow
#pygame.draw.circle(screen, (0, 0, 0))	  # Black
#pygame.draw.circle(screen, (0, 255, 0))	  # Green
#pygame.draw.circle(screen, (255, 0, 0))	  # Red
##
#running = True
#pygame.display.flip()
#for event in pygame.event.get():
#		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key ==pygame.K_q):
#			run = False
####