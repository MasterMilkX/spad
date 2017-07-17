import pygame
from random import randint

#SCREEN VARIABLES
SCREEN_SIZE = 250
SPAD_SIZE = 100
OFFSET = (SCREEN_SIZE - SPAD_SIZE) / 2
EYE_SIZE = SPAD_SIZE / 5
onscreen = True

#PALETTE
GAMEBOY_PALETTE = [[155, 188, 15],[139, 172, 15], [48, 98, 48], [15, 56, 15], [0,0,0]]
GRAYSCALE_PALETTE = [[200, 200, 200], [150, 150, 150], [100, 100, 100, 100], [50, 50, 50], [0,0,0]]
PALETTE = GRAYSCALE_PALETTE

#SPAD VARIABLES
face = "neutral"
blinking = False
OPEN = pygame.USEREVENT+1
CLOSE = pygame.USEREVENT+2

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("SPAD")


def main():
	play = True
	pygame.time.set_timer(CLOSE, 2000)
	pygame.time.set_timer(OPEN, 100)

	while play:
		global face
		global blinking
		global onscreen

		onscreen = bool(pygame.mouse.get_focused())

		#interaction events
		for event in pygame.event.get():
			#close window functions
			if event.type == pygame.QUIT:
				play = False

			#neutral-blinking functions
			if onscreen:
				if event.type == OPEN:
					if(blinking):
						blinking = False
						face = "neutral"
				elif event.type == CLOSE:
					if(not blinking):
						blinking = True
						face = "closed_eyes"
		#draw
		screen.fill(PALETTE[0])
		spad(0, 0, 0, 0)
		pygame.display.flip()


def spad(x, y, ex, ey):
	ox = OFFSET + x
	oy = OFFSET + y
	#body
	pygame.draw.rect(screen, (PALETTE[1]), pygame.Rect(ox, oy, SPAD_SIZE, SPAD_SIZE))
	#eyes
	if(face == "neutral"):
		pygame.draw.rect(screen, (PALETTE[2]), pygame.Rect(ox + EYE_SIZE, oy + (2*EYE_SIZE), EYE_SIZE, EYE_SIZE))
		pygame.draw.rect(screen, (PALETTE[2]), pygame.Rect(ox + (3*EYE_SIZE), oy + (2*EYE_SIZE), EYE_SIZE, EYE_SIZE))
	elif(face == "closed_eyes"):
		pygame.draw.rect(screen, (PALETTE[2]), pygame.Rect(ox + EYE_SIZE, oy + ((5/2)*EYE_SIZE), EYE_SIZE, EYE_SIZE/4))
		pygame.draw.rect(screen, (PALETTE[2]), pygame.Rect(ox + (3*EYE_SIZE), oy + ((5/2)*EYE_SIZE), EYE_SIZE, EYE_SIZE/4))



main()
