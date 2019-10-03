import module21
import datetime
i = input('choose act date or numbers: ')
if i == 'numbers':
	numb0 = input('Enter Number: ')
	command = input('Endter command: ')
	result = numb0
	while True:
		numb1 = input('Enter Number: ')
		if numb1 == 'q':
			print('End programm')
			break
		result = module21.calcnumb(a = numb1, do = command, c = result)
		command = input('Endter result or command: ')
		if command == 'result':
			if result == None:
				print('0')
			print(result)
			break
		elif command == 'q':
			print('End programm')
			break
elif i == 'date':
	while True:
		d1 = datetime.date(int(input('Y: ')),int(input('M: ')),int(input('D: ')))
		print(d1)
		act = input('Enter act(+ or -): ')
		d2 = datetime.date(int(input('Y: ')),int(input('M: ')),int(input('D: ')))
		print(d2)
		res = module21.calcdate( do = act, c = d1, a = d2)
		print(res)
		k = input('End programm?(y)')
		if k == 'y':
			print('End programm')
			break

