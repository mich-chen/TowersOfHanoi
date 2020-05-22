from stack import Stack

print("Let's play Towers of Hanoi!")

#Creating the stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack, middle_stack, right_stack]
#test below
#print(stacks[0].get_name())

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

#integer of user's input
#game must have 3 or more disks to play
while num_disks < 3:
	num_disks = int(input("Enter a number greater than or equal to 3.\n"))

for disk in range(num_disks, 0, -1):
	left_stack.push(disk)

num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves.".format(num_optimal_moves))

#Get User Input
def get_input():
	choices = [stack.get_name()[0] for stack in stacks]
	#test below
	#print(choices)
	#choices = ["l", "M", "R"]
	while True:
		for i in range(len(stacks)):
			#for i in (0, 1, 2)
			name = stacks[i].get_name()
			letter = choices[i]
			print("Enter {0} for {1}".format(letter, name))
		user_input = input("")
		if user_input in choices:
			for i in range(len(stacks)):
				if user_input == choices[i]:
					return stacks[i]

#Play the game

num_user_moves = 0
#keeps track of number of user's moves
while right_stack.get_size() != num_disks:
	#as long as right stack does not contain total number of disks (meaning the game has ended)
	print("\n\n...Current Stacks...")
	for stack in stacks:
		stack.print_items()
	while True:
		print("\nWhich stack do you want to move FROM?\n")
		from_stack = get_input()
		print("\nWhich stack do you want to move TO?\n")
		to_stack = get_input()
		
		if from_stack.is_empty():
			#if stack.value == 0
			print("\n\nInvalid move. Cannot remove from an empty stack. Try again.")
			print("\n...Current Stacks...")
			for stack in stacks:
					stack.print_items()
		elif (to_stack.is_empty()) or (from_stack.peek() < to_stack.peek()):
			# valid moves: if TO stack is empty or if disk size in FROM stack is < disk in TO stack.
			disk = from_stack.pop()
			to_stack.push(disk)
			num_user_moves += 1
			break
		else:
			print("\n\nInvalid Move. Cannot put bigger disk onto smaller disk. Try Again.")
			print("\n...Current Stacks...")
			for stack in stacks:
					stack.print_items()

print("\n\nCongrats! You completed the game in {0} moves, and the optimal number of moves is {1}!".format(num_user_moves, num_optimal_moves))
