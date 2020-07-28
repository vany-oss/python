valores = list()
for cont in range(0, 5):
	valores.append(str(input('Procure o seu Alvo ')))
	
for c, v in enumerate(valores):
	print(f'\033[32mNa posicao {c} encontrei {v}\033[m')
	if  valores[c] == 'netcha':
		print(f'\033[36mSucesso. Encontrei o alvo na posisao {c}\033[m')
		break

	else:
		 print('\033[31mSEM SUCESSO NÃO ENCONTREI  ALVO.\033[m')
print('Fim...')