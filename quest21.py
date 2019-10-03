import module21
numb0 = input('Enter Number: ')
command = input('Endter command: ')
result = numb0
while True:
	numb1 = input('Enter Number: ')
	if numb1 == 'q':
		print('End programm: ')
		break
	result = module21.calc(a = numb1, do = command, c = result)
	command = input('Endter result or command: ')
	if command == 'result':
		if result == None:
			print('0')
		print(result)
		break
	elif command == 'q':
		print('End programm')
		break
