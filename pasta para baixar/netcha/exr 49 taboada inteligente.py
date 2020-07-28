n  = int(input('digite um numero para ver a sua taboada! '))
for c in range(1, 11):
	print('{} x {:2} = {}'.format(n, c, n*c))