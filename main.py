print('''
*************************

Welcome to Sorting Hat. I'm smart, elegant and fast.
Version 0.5

*************************
''')

user_path = input('Drag a folder you want to work with inside this window: ')
directory_path = user_path.strip()

while True:
	'''Context menu to choose which action to apply to the folder'''
	user_action = input('''Please choose an action:
[F]ind duplicates | [S]ort files in the folder | [E]xit  : ''').lower()
	if user_action == 'f':
		print('Finding duplicates...')
	elif user_action == 's':
		print('Sorting files...')
	elif user_action == 'e':
		print('Thank you for using Sorting Hat App. Have a great day!')
		break
	else:
		print('There is something wrong with your answer. Please try again')