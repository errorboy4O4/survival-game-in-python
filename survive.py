import pygame 
import math

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
pink = (255, 0, 255)
blue = (0, 0, 255)
aqua = (0, 255, 255)
red = (245, 66, 66)
gold = (245, 242, 66)

width = 800
height = 600
WORD_FONT = pygame.font.SysFont("comicsans", 60)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('SURVIVE')

# HERO SIZE
hero_x = 100
hero_y = 300

# HERO SPEED
hero_x_speed = 0
hero_y_speed = 0

# HERO IMAGE
hero_img = pygame.image.load('ironman.png')

# ENEMY IMAGE
enemy_img = pygame.image.load('thanos1.png')

# ENEMY SIZE
enemy_x = 550
enemy_y = 300

# ENEMY SPEED
enemy_x_speed = 0
enemy_y_speed = 0

# BULLET IMAGE
bullet_img = pygame.image.load('hammer.png')

# BULLET SIZE
bullet_x = 10
bullet_y = 525
bullet_state = 'ready'
bullet_x_change = 3
bullet_y_change = 3

# ENEMY WEPON IMAGE
enemy_wepon_img = pygame.image.load('sword.png')

# ENEMY WEPON SIZE
enemy_wepon_x = 730
enemy_wepon_y = 525
enemy_wepon_state = 'ready'
enemy_wepon_x_change = 3
enemy_wepon_y_change = 3

# HERO SCORE
hero_score = 10
enemy_score = 10

font = pygame.font.Font('freesansbold.ttf', 25)

hero_text_x = 10
hero_text_y = 10

enemy_text_x = 635
enemy_text_y = 10

def hero_show_score(x, y):
	score = font.render("HEALTH: " + str(hero_score), True, (red))
	win.blit(score, (x, y))

def enemy_show_score(x, y):
	score = font.render("HEALTH: " + str(enemy_score), True, (gold))
	win.blit(score, (x, y))


def fire_bullet(x, y):
	global bullet_state
	bullet_state = 'fire'
	win.blit(bullet_img, (x + 10, y + 15))

def enemy_fire_bullet(a, b):
	global enemy_wepon_state
	enemy_wepon_state = 'fire'
	win.blit(enemy_wepon_img, (a + 10, b + 15))

def enemy_is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
	distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2)) 
	if distance < 27:
		return True
	else:
		return False

def hero_is_collision(hero_x, hero_y, enemy_wepon_x, enemy_wepon_y):
	distance = math.sqrt(math.pow(hero_x - enemy_wepon_x, 2) + math.pow(hero_y - enemy_wepon_y, 2)) 
	if distance < 27:
		return True
	else:
		return False

def display_msg(message):
	win.fill(white)
	text = WORD_FONT.render(message, 1, green)
	win.blit(text, (350, 250))
	pygame.display.update()
	pygame.time.delay(2000)

run = False

while not run:
	win.fill(aqua)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				hero_x_speed += 2
			if event.key == pygame.K_LEFT:
				hero_x_speed -= 2
			if event.key == pygame.K_UP:
				hero_y_speed -= 2
			if event.key == pygame.K_DOWN:
				hero_y_speed += 2

		if event.type == pygame.KEYUP:
			 if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
			 	hero_x_speed = 0
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			 	hero_y_speed = 0


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				enemy_y_speed -= 2
			if event.key == pygame.K_s:
				enemy_y_speed += 2
			if event.key == pygame.K_a:
				enemy_x_speed -= 2
			if event.key == pygame.K_d:
				enemy_x_speed += 2

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_s:
			 	enemy_y_speed = 0
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d or event.key == pygame.K_a:
			 	enemy_x_speed = 0

# BULLET MOVEMENT

			if event.key == pygame.K_SPACE:
				if bullet_state == 'ready':
					bullet_y = hero_y
					bullet_x = hero_x
					fire_bullet(bullet_x, bullet_y)

			if event.key == pygame.K_RETURN:
				if enemy_wepon_state == 'ready':
					enemy_wepon_y = enemy_y
					enemy_wepon_x = enemy_x
					enemy_fire_bullet(enemy_wepon_x, enemy_wepon_y)


	hero_x += hero_x_speed
	hero_y += hero_y_speed

	enemy_x += enemy_x_speed
	enemy_y += enemy_y_speed

	# BULLET BOUNDARY CHECK

	if bullet_x >= 730:
		bullet_x = 10
		bullet_state = 'ready'

	if bullet_state == 'fire':
		fire_bullet(bullet_x, bullet_y)
		bullet_x += bullet_x_change

	if enemy_wepon_x <= 10:
		enemy_wepon_x = 730
		enemy_wepon_state = 'ready'

	if enemy_wepon_state == 'fire':
		enemy_fire_bullet(enemy_wepon_x, enemy_wepon_y)
		enemy_wepon_x -= enemy_wepon_x_change

	# HERO BOUNDARY CHECK

	if hero_y < 0:
		hero_y = 0
	elif hero_y >= 525:
		hero_y = 525
	if hero_x <= 10:
		hero_x = 10
	if hero_x >= 330:
		hero_x = 330

# ENEMY BOUNDARY CHECK

	if enemy_y < 0:
		enemy_y = 0
	elif enemy_y >= 525:
		enemy_y = 525 
	if enemy_x >= 730:
		enemy_x = 730
	if enemy_x <= 425:
		enemy_x = 425

# COLLISION CHECK

	enemy_collision = enemy_is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
	if enemy_collision:
		bullet_x = 10
		bullet_state = 'ready'
		enemy_score -= 1
		
	enemy_collision = enemy_is_collision(hero_x, hero_y, enemy_wepon_x, enemy_wepon_y)
	if enemy_collision:
		enemy_wepon_x = 10
		enemy_wepon_state = 'ready'
		hero_score -= 1

	if hero_score == 0:
		display_msg('BLUE WIN')
		break
	if enemy_score == 0:
		display_msg('RED WIN')
		break

	pygame.draw.rect(win, black, (400, 0, 20, 600))
	hero_show_score(hero_text_x, hero_text_y)
	enemy_show_score(enemy_text_x, enemy_text_y)
	win.blit(hero_img, (hero_x, hero_y))
	win.blit(enemy_img, (enemy_x, enemy_y))
	
	pygame.display.update()
pygame.quit()

