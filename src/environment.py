class Environment:
	OBSTACLE = -1
	MAP_ROAD = '-'
	MAP_OBSTACLE = 'O'
	CLEAN_PER_TIME = 10	


	#Initial position, dirty probability, random seed, map
	size = 0
	positionX = 0
	positionY = 0
	dirty = 0
	seed = 0
	map_num = 0

	maze = []

	def __init__(self,f):
		params = [float(x) for x in f.readline().split(' ')]
		self.size = params[0]
		self.positionX = params[1]
		self.positionY = params[2]
		self.dirty = params[3]
		self.seed = params[4]
		for itt in range(int(self.size)):
			line = f.readline()
			y = 0
			l = []
			for sym in line:
				if sym != ' ' and sym != '\n':
					if y < self.size: 
						if sym == self.MAP_ROAD:
							l.append(0)
						elif sym == self.MAP_OBSTACLE:
							l.append(self.OBSTACLE)
						y+=1
						# print y,l
			self.maze.append(l)
		for line in self.maze:
			print [' %s ' % x for x in line]
	def dirt_amout(x,y):
		if self.maze[x][y] == OBSTACLE:
			return 0
		return maze[x][y]


