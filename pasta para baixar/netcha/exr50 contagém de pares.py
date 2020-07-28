soma = 0
cont = 0
for c in range(1, 7):
	nun = int(input('digite o {}° valor '.format(c)))
	if nun % 2 == 0:
		soma += nun
		cont += 1
print(f'voce informou {cont} nrs pares  e a soma é {soma}')