from environment import OBSTACLE

class Evaluator:
	dirty_degree = 0 
	consumed_energy = 0 
	total_dirty = 0 
	cleaned_dirty = 0 
	new_dirty = 0
	LIFE_TIME = 0

	def __init__(self):
		self.LIFE_TIME = 2000

	def evaluete(self, action, env):
		if action == 'SUCK':
			self.consumed_energy += 2
		elif action != 'IDLE':
			self.consumed_energy +=1
		self.cleaned_dirty += env.cleaned_dirt
		self.new_dirty = env.new_dirt
		self.total_dirty += self.new_dirty

		dirty_degree = 0
		for item in env.maze:
			for el in item:
				if el != OBSTACLE:
					dirty_degree += el