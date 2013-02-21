OBSTACLE = -1
MAP_ROAD = '-'
MAP_OBSTACLE = 'O'
CLEAN_PER_TIME = 10	

class Environment:
	#Initial position, dirty probability, random seed, map
	size = 0
	positionX = 0
	positionY = 0
	dirty = 0
	seed = 0
	map_num = 0

	maze = []

	bump = False
	cleaned_dirt = 0
	new_dirt = 0

	def __init__(self,f):
		params = [float(x) for x in f.readline().split(' ')]
		self.size = params[0]
		self.positionX = int(params[1])
		self.positionY = int(params[2])
		self.dirty = params[3]
		self.seed = params[4]
		for itt in range(int(self.size)):
			line = f.readline()
			y = 0
			l = []
			for sym in line:
				if sym != ' ' and sym != '\n':
					if y < self.size: 
						if sym == MAP_ROAD:
							l.append(0)
						elif sym == MAP_OBSTACLE:
							l.append(OBSTACLE)
						y+=1
			self.maze.append(l)

		from main import DEBUG
		if DEBUG:
			for line in self.maze:
				print ['{0:3}'.format(x) for x in line]
	
	def dirt_amout(self,x,y):
		if self.maze[x][y] == OBSTACLE:
			return 0
		return maze[x][y]

	def accept_action(self,action):
		self.bump = False
		self.cleaned_dirt = 0
		if action == 'UP':
			if self.maze[self.positionX-1][self.positionY] != OBSTACLE: 
				self.positionX -=1
			else:
				self.bump = True
		if action == 'DOWN':
			if self.maze[self.positionX+1][self.positionY] != OBSTACLE: 
				self.positionX +=1
			else:
				self.bump = True
		if action == 'LEFT':
			if self.maze[self.positionX][self.positionY-1] != OBSTACLE:
				self.positionY -=1
			else:
				self.bump = True
		if action == 'RIGHT':
			if self.maze[self.positionX][self.positionY+1] != OBSTACLE: 
				self.positionY +=1
			else:
				self.bump = True
		if action == 'SUCK':
			if maze[self.positionX][self.positionY] > 0:
				if maze[self.positionX][self.positionY] > self.CLEAN_PER_TIME:
					self.cleaned_dirt = self.CLEAN_PER_TIME 
				else:
					self.cleaned_dirt = self.maze[positionX][positionY]
	
	def is_dirty(self):
		return self.maze[self.positionX][self.positionY] > 0

	def is_bump(self):
		return self.bump

	def change():
		import random
		self.new_dirty = 0
		for pos in maze:
			if pos != OBSTACLE and (random.random()/random.random()) < self.dirt*100:
				pos += 1
				self.new_dirty +=1

