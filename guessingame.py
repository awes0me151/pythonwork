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
        if int(bet) > money:
			print("You cannot do this! Insufficient funds.")
		else:
			if int(guess) == num:
            	money += int(bet)
				print("You guessed correctly. " + "You now have " + str(money) + ".")
  			else:
				money -= int(bet)
                print("You guessed incorrectly. " + "You now have " + str(money)+ ".")
	else:
		print ("Try again")

quit = False
while not quit:
	print("You have " + str(money) + ".")
    if money == 0:
      print("Game over!")
      quit = True
    else:
      choice = input('Would you like to continue? (Y/N) ')
      if choice.upper().strip() == 'Y' or choice.upper().strip() == 'YES':
          bet_input = input('How much money would you like to bet? ')
          guess_input = input('What side would you like to guess? (1/2) ')
          coin_flip(guess_input, bet_input)
      else:
          quit = True
