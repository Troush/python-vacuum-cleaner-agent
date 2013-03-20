from optparse import OptionParser

from environment import Environment as env
from agent import Agent
from evaluator import Evaluator
DEBUG = True


def run(zone, agent, calculus):
	zone.change()

	agent.prespective(zone)

	action = agent.think()
	print action
	zone.accept_action(action)
	calculus.evaluete(action,zone)
	zone.print_maze()

def main():
	f = open(map_path)
	zone = env(f)
	bond = Agent(zone)
	current_time = 0
	calculus = Evaluator()

	while current_time < life_time:
		run(zone,bond,calculus)
		current_time+=1

if __name__ == "__main__":
	current_time = 0
	life_time = 100
	map_path = '../map/first.map'

	usage = "usage: %prog [options] arg1 arg2"
	parser = OptionParser(usage=usage)
	parser.add_option("-m", "--map", dest="map_path", default=False,
                  help="Path to the map")
	parser.add_option("-l", "--life", dest="life_time", default=False,
                  help="Life time value")
	args = parser.parse_args()
	args = args[0]

	if args.map_path:
		map_path = args.map_path
	if args.life_time:
		life_time = int(args.life_time)

	main()
