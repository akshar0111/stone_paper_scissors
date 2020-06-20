import numpy as np

def display_computer_move(move):
	if move == 1:
		print('COMPUTER MOVE:: STONE\n')
	elif move == 2:
		print('COMPUTER MOVE:: PAPER\n')
	else:
		print('COMPUTER MOVE:: SCISSOR\n')

def display_winner(user_move):
	computer_move = np.random.randint(1,4)
	#comparing moves
	if (computer_move == user_move):
		display_computer_move(computer_move)
		print('MATCH TIE\n')

	elif computer_move == 1 and user_move == 2:
		display_computer_move(computer_move)
		print('YOU WIN :) \n')
	elif computer_move == 2 and user_move == 3:
		display_computer_move(computer_move)
		print('YOU WIN :) \n')
	elif computer_move == 3 and user_move == 1:
		display_computer_move(computer_move)
		print('YOU WIN :) \n')

	elif computer_move == 2 and user_move == 1:
		display_computer_move(computer_move)
		print('COMPUTER WINS \n')
	elif computer_move == 3 and user_move == 2:
		display_computer_move(computer_move)
		print('COMPUTER WINS \n')
	elif computer_move == 1 and user_move == 3:
		display_computer_move(computer_move)
		print('COMPUTER WINS \n')
	else:
		print('Invalid move :/')
def main():
	print('#'*40)
	print('\n       hey welcome \n')
	print('#'*40)
	print('FOR STONE PRESS-   "1"\n')
	print('FOR PAPER PRESS-   "2"\n')
	print('FOR SCISSOR PRESS- "3"\n')
	counter = 'y'
	while(counter == 'y' or counter == 'Y'):
		user_input = int(input('ENTER YOUR MOVE:: '))
		display_winner(user_input)

		counter = input('\ndo you want to play again ? press "y" for yes and "n" for no\n')
		print('_'*40)

if __name__ == '__main__':
	main()

