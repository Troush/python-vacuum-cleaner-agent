class Agent:
	bump = False
	dirty = False
	msg = ''

	def __init__(self):
		self.msg = 'Hello World, i\'m Vacuum'

	def up(self):
		return "UP"

	def down(self):
		return "DOWN"

	def left(self):
		return "LEFT"

	def right(self):
		return "RIGHT"

	def suck(self):
		return "SUCK"

	def idle(self):
		return "IDLE"

	def prespective(self,env):
		self.bump = env.bump
		self.dirty = env.dirty

	def think(self):
		pass

		