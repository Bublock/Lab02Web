def work5():
	value = int(input('Введите целое число: '))
	if value < 2:
		print('False')
		return False
	if value == 2:
		print('True')
		return True
	lim = value**(1/2)
	i=2
	while (i <= lim):
		if value%i == 0:
			print('False')
			return False
		i+=1
	print('True')
	return True
work5()
