OBSTACLE = '-1'
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
		self.size = int(params[0])
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

	def dirt_amout(self,x,y):
		if self.maze[x][y] == OBSTACLE:
			return 0
		return self.maze[x][y]

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
			if self.maze[self.positionX][self.positionY] > 0:
				dirt = self.maze[self.positionX][self.positionY]
				if dirt > CLEAN_PER_TIME:
					self.cleaned_dirt = dirt
					self.maze[self.positionX][self.positionY] =\
						dirt - CLEAN_PER_TIME
				else:
					self.cleaned_dirt = dirt
					self.maze[self.positionX][self.positionY] = 0

	def is_dirty(self):
		return self.maze[self.positionX][self.positionY] > 0

	def is_bump(self):
		return self.bump

	def change(self):
		import random
		self.new_dirty = 0
		for idx,row in enumerate(self.maze):
			for idy,col in enumerate(row):
				if col != OBSTACLE and (random.random()/self.seed) < self.dirty:
					self.maze[idx][idy] = 1
					self.new_dirty +=1

	def print_maze(self):
		value = self.maze[self.positionX][self.positionY]
		self.maze[self.positionX][self.positionY] = '|@|'
		print '|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|'
		for line in self.maze:
			print ['{0:3}'.format(x) for x in line]
		print '|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|===|\n'
		self.maze[self.positionX][self.positionY] = value

