import random

money = 700

def RepresentsInt(a):
	try:
		int(a)
		return True
	except ValueError:
		return False

def test_positive(number):
	return (int(number) > 0)

# Coin Flip Game
def coin_flip(guess, bet):
	if RepresentsInt(bet) and test_positive(bet):
		global money
		num = random.randint(1,2)
		if int(guess) == num:
			money += int(bet)
			print("You guessed correctly. " + "You now have " + str(money) + ".")
		else:
			money -= int(bet)
			print("You guessed incorrectly. " + "You now have " + str(money)+ ".")
	else:
		print ("Wait a second, you made a wrong bet. Try again please.")

print("Welcome to my game! Starting with 700 dollars, you bet your money on either 1 or 2. \nIf you guess correctly, you win the money you bet, and if you are incorrect, you lose the money you bet! \nCheating is not allowed!")
print("You have " + str(money) + ".")
while True:
	if money == 0:
		exit("Game over!")
	else:
		choice = input('Would you like to continue? (Y/N) ')
		if choice.upper().strip() == 'Y' or choice.upper().strip() == 'YES':
			bet_input = input('How much money would you like to bet? ')
			bad_input = not bet_input.isdigit() or int(bet_input) > money or int(bet_input) <= 0
			if bad_input:
				print ("You're cheating! I'm giving you one more chance.")
				bet_input = input('So, how much will you bet this time, cheater? ')
				bad_input = not bet_input.isdigit() or int(bet_input) > money or int(bet_input) <= 0
				if bad_input:
					exit("Game over, cheater!")
				else:
					bet_input = int(bet_input)
					guess_input = input('What side would you like to guess? (1/2) ')
					if guess_input == '1' or guess_input == '2':
						coin_flip(guess_input, bet_input)
					else:
						print("Choose either 1 or 2.")
						guess_input = input('What side would you like to guess? (1/2) ')
						if guess_input == '1' or guess_input == '2':
							coin_flip(guess_input, bet_input)
						else:
							exit("Since you can't follow rules, this game isn't for you!")
			else:
				bet_input = int(bet_input)
				guess_input = input('What side would you like to guess? (1/2) ')
				if guess_input == '1' or guess_input == '2':
					coin_flip(guess_input, bet_input)
				else:
					print ("Choose either 1 or 2.")
					guess_input = input('What side would you like to guess? (1/2)')
					if guess_input == '1' or guess_input == '2':
						coin_flip(guess_input, bet_input)
					else:
						exit("Since you can't follow rules, this game isn't for you!")
		else:
			exit("Goodbye! You ended the game with " + str(money) + " dollars.")
