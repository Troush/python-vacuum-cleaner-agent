from environment import Environment as env
def main():
	f = open('../map/first.map')
	zone = env(f)
	print zone.__dict__


if __name__ == "__main__":
    main()