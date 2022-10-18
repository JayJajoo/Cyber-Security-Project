import random
from math import pow

def main():

	q = random.randint(pow(10, 20), pow(10, 50))
	g = random.randint(2, q)

	file=open("elgamal_keys.txt","w")
	file.write("{0}\n{1}\n".format(q,g))
	file.close()

if __name__ == '__main__':
	main()
