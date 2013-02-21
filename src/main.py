from environment import Environment as env
from agent import Agent
from evaluator import eval
DEBUG = True


def run(zone, agent):
	zone.change

	agent.prespective(zone)
	print agent.bump, agent.dirty

	action = agent.think()
	zone.accept_action('DOWN')


def main():
	f = open('../map/first.map')
	zone = env(f)
	bond = Agent()
	print zone.__dict__
	current_time = 0

	while current_time < life_time:
		run(zone,bond)
		current_time+=1

if __name__ == "__main__":
	current_time = 0
	life_time = 100
	main()