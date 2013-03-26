from environment import Environment
class Agent:
	bump = False
	dirty = False
	msg = ''
	agent_map = []
	last_action = None
	posX = 0
	posY = 0

	def __init__(self,zone):
		self.msg = 'Hello World, i\'m Vacuum'
		self.agent_map = [[0 for col in range(zone.size*2)] for row in range(zone.size*2)]
		self.posX = zone.positionX
		self.postY = zone.positionY

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
		self.dirty = env.dirt_amout(self.posX,self.posY)
		self.posX, self.posY = env.positionX, env.positionY

	def think_dummy(self):
		import random
		if self.dirty > 0.1:
			return self.suck()
		actions = [self.up(),self.down(),self.left(),self.right()]
		return actions[int(random.random()*4)]

	def think(self):
		pass
