import random

x = "y"

while x == "y":
	
	# Gnenerates a random number
	# between 1 and 6 (including
	# both 1 and 6)
	
	print(random.randint(1,6))
		
	x=input("press y to roll again and n to exit:\n")
