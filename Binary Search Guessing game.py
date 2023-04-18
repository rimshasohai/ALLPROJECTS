print("Please think of a number between 0 and 100!")


upperbound = 100
lowerbound = 0
while True:
	mid = (upperbound - lowerbound)/2 + lowerbound
	
	print("Is your secret number %s?" % round(mid,1))
	guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if guess == 'h':
		upperbound = mid
	elif guess == 'l':
		lowerbound = mid
	elif guess == 'c':
		print('Game over. Your secret number was: ' + str(mid))
		break
	else:
		print('Sorry, I did not understand your input.')
