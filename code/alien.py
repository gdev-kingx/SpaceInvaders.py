import pygame as pg

class Alien(pg.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = '/Users/rsarvesh/Downloads/Python/Space Invaders/graphics/' + color + '.png'
        self.image = pg.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))

        if color == 'red': self.value = 100
        elif color == 'green': self.value = 200
        else: self.value = 300
    
    def update(self,direction):
        self.rect.x += direction

class Extra(pg.sprite.Sprite):
	def __init__(self,side,screen_width):
		super().__init__()
		self.image = pg.image.load('/Users/rsarvesh/Downloads/Python/Space Invaders/graphics/extra.png').convert_alpha()
		
		if side == 'right':
			x = screen_width + 50
			self.speed = - 3
		else:
			x = -50
			self.speed = 3

		self.rect = self.image.get_rect(topleft = (x,80))

	def update(self):
		self.rect.x += self.speed