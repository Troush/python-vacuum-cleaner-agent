from environment import Environment as env
from agent import Agent
from evaluator import Evaluator
DEBUG = True


def run(zone, agent, calculus):
	zone.change

	agent.prespective(zone)

	action = agent.think()
	print action
	zone.accept_action(action)
	calculus.evaluete(action,zone)
	zone.print_maze()

def main():
	f = open('../map/first.map')
	zone = env(f)
	bond = Agent()
	current_time = 0
	calculus = Evaluator()

	while current_time < life_time:
		run(zone,bond,calculus)
		current_time+=1

if __name__ == "__main__":
	current_time = 0
	life_time = 100
	main()