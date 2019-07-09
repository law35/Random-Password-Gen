##
"""Random Password:"""
import random
from random import randint
shortest = 4
longest = 4

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
	'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
	'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
	'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
	'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

PW_library = []

def password_gen():
	#Generates a length limit for the password:
	randomLength = randint(shortest, longest)
	password = ""
	
	for i in range(randomLength):
		numeric = random.choice(numbers)#:Chooses a random number from numbers.
		alpha = random.choice(letters)#:Chooses a random letter from letters.
		randomChar = (alpha + numeric)#:Splices the choices from alpha and numeric.
		password += randomChar
	#Stores the new pw in PW_library:
	PW_library.append(password)

	print "Pw stored as: %s" % PW_library
	return password
	
if __name__ == '__main__':
	while True:
		print ("Your password is: %s" % password_gen())
		a = str(raw_input("Do you wish to quit?(Y or N):>> ").upper())
		if a == 'Y' or a == 'y':
			break