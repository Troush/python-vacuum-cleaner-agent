from environment import Environment
class Agent:
	bump = False
	dirty = False
	msg = ''
	agent_map = []
	agent_map_time = []
	last_action = None
	posX = 0
	posY = 0
	map_is_full = False
	move_num = 0
	zone_size = 0
	curentTime = 0
	point_count = 0

	def __init__(self,zone):
		self.msg = 'Hello World, i\'m Vacuum'
		self.agent_map = [[0 for col in range(zone.size*2)]\
							 for row in range(zone.size*2)]
		self.posX = zone.positionX
		self.postY = zone.positionY
		self.educate()
		self.zone_size = zone.size
		self.curentTime = 0

	def up(self):
		last_action = "UP"
		return "UP"

	def down(self):
		last_action = "DOWN"
		return "DOWN"

	def left(self):
		last_action = "LEFT"
		return "LEFT"

	def right(self):
		last_action = "RIGHT"
		return "RIGHT"

	def suck(self):
		last_action = "SUCK"
		return "SUCK"

	def idle(self):
		last_action = "IDLE"
		return "IDLE"

	def prespective(self,env):
		self.bump = env.bump
		self.dirty = env.dirty
		self.posX, self.posY = env.positionX, env.positionY

	def think_dummy(self):
		import random
		if self.dirty > 0.1:
			return self.suck()
		actions = [self.up(),self.down(),self.left(),self.right()]
		return actions[int(random.random()*4)]

	def educate(self):
		if self.agent_map_time[self.posX][self.posY] > 0:
			self.point_count += 1
		self.agent_map_time[self.posX][self.posY] = self.curentTime

	def place_wall(self):
		self.agent_map[self.posX][self.posY] = 'O'

	def place_space(self):
		self.agent_map[self.posY][self.posY] = '-'

	def wall_action(self):
		import random
		actions_list = [self.up(),self.down(),self.left(),self.right()]
		action = actions_list[int(random.random()*4)]
		if self.last_action != action:
			return action
		self.wall_action()

	def is_all_map(self):
		count = 0
		for item in self.agent_map_time:
			if item > 0:
				count += 1
		if count > self.zone_size ** 2:
			return True
		return False

	def think(self):
		if self.agent_map:
			if self.bump:
				self.place_wall()
				return self.wall_action()
			if self.dirty:
				return self.suck()
		self.educate()
		self.move_num += 1
		self.curentTime += 1
		return None

def pos_in_dict(x,y,item):
	if x == item.get('x'):
		if y == item.get('y'):
			return True
		return False
