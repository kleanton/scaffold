import pygame, sys, time, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH=400
WINDOWHEIGHT=400

windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Игра смурф смурфный')

WHITE = (255,255,255)

player = pygame.Rect(300,100,50,40)
playerImage = pygame.image.load('/pic/smurf.png')
playerStretchedImage = pygame.transform.scale(playerImage,(40,40))
foodImage = pygame.image.load('/pic/apple.png')
foods = []
for i in range(20):
	foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-20),random.randint(0,WINDOWHEIGHT-20),20,20))

foodCounter=0
NEWFOOD = 40

moveLeft=False
moveRight=False
moveUp=False
moveDown=False

MOVESPEED = 6

pickUpSound= pygame.mixer.Sound('/sound/pickup.wav')
pygame.mixer.music.load('/sound/background.mid')
pygame.mixer.music.play(-1,0.0)
musicPlaying = True

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT or event.key == K_a:
				moveRight = False
				moveLeft = True
			if event.key == K_RIGHT or event.key == K_d:
				moveRight = True
				moveLeft = False
			if event.key == K_UP or event.key == K_w:
				moveUp = True
				moveDown = False
			if event.key == K_DOWN or event.key == K_s:
				moveDown = True
				moveUp = False
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_LEFT or event.key == K_a:
				moveLeft = False
			if event.key == K_RIGHT or event.key == K_d:
				moveRight = False
			if event.key == K_UP or event.key == K_w:
				moveUp = False
			if event.key == K_DOWN or event.key == K_s:
				moveDown = False
			if event.key == K_x:
				player.top = random.randint(0,WINDOWHEIGHT-player.height)
				player.left = random.randint(0,WINDOWWIDTH - player.width)
			if event.key == K_m:
				if musicPlaying:
					pygame.mixer.music.stop()
				else:
					pygame.mixer.music.play(-1,0.0)
				musicPlaying = not musicPlaying
		if event.type == MOUSEBUTTONUP:
			foods.append(pygame.Rect(event.pos[0]-10,event.pos[1]-10,20,20)

	#foodCounter+=1
	if foodCounter >= NEWFOOD:
		foodCounter = 0
		foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-20),random.randint(0,WINDOWHEIGHT-20),20,20))
	
	windowSurface.fill(WHITE)
	backgroundSurface= pygame.Rect(0,0,400,400)
	backgroundPic= pygame.image.load('/pic/background.png')
	backgroundStretchedImage=pygame.transform.scale(backgroundPic,400,400)

	if moveDown and player.bottom < WINDOWHEIGHT:
		player.top +=MOVESPEED
	if moveUp and player.top >0:
		player.top -=MOVESPEED
	if moveLeft and player.left >0:
		player.left -= MOVESPEED
	if moveRight and player.right < WINDOWWIDTH:
		player.right +=MOVESPEED

	windowSurface.blit(backgroundStretchedImage,backgroundSurface)
	windowSurface.blit(playerStretchedImage,player)

	for food in foods[:]:
		if player.colliderect(food):
			foods.remove(food)
			player=pygame.Rect(player.left,player.top,player.width+2,player.height+2)
			playerStretchedImage=pygame.transform.scale(playerImage,(player.width,player.height))
			if musicPlaying:
				pickUpSound.play()

	for food in foods:
		windowSurface.blit(foodImage,food)
	pygame.display.update()
	mainClock.tick(40)


			