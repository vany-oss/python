total = 0
while True:
	print('{:-^43}'.format('Loja Elma:'))
	p = str(input('Artigo: '))
	prs = float(input('Preço R$: '))
	total += prs
	res = ' '
	while res not in 'SN':
		res = str(input('Queres Continuar [S/N] ? ')).strip().upper()[0]
	if res == 'N':
		break
print('{:-^40}'.format('Fim da compra'))
print(f'No total as tuas compras são de {total} euros.')

#sistema de loja