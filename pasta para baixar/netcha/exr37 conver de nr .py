num = int(input('digite um numero inteiro '))
print('''escolha uma das opcao para converter:
[1 ] Binario
[2 ] Octal
[3 ] Hexadeximal  ''')
	
op = int(input('qual e a sua opcao? '))
if op == 1:
	print('{} convertido em Binario é {}'.format(num, bin(num)[2:]))
elif op == 2:
	print('{} convertido em Octanal é {}'.format(num, oct(num)[2:]))
elif op == 3:
	print('{} convertido em Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
	print('Opcao Invalida Tente outra vez!')
	
# pg que conver os numeros em b oct hex
