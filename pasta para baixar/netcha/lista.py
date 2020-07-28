a = [2, 4, 6, 4 ,9]
b = a[:]
b[0] = 8

a.append(7)
print(f'lista A: {a}')
print(f'lista B: {b}')
if 10 in a:
	print('sucesso Consegui..Ele esta aqui.')
else:
	print('\033[31msem sucesso.. Nao encontrei o nr 10..\033[m')