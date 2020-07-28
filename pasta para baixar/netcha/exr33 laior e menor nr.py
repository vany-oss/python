a = int(input('primeiro numero? '))
b = int(input('segundo numero? '))
c = int(input('terceiro numero? '))
menor = a 
if b < a and b < c:
	menor = b
if c < a and c< b:
	menor = c
	# verificar maior 
maior = a 
if b > a and b > c:
	maior = b 
if c>a and c>b:
	maior = c
print('o maior valor digitado é {}'.format(maior))
print('o menor valor digitado é {}'.format(menor))

# pg que le 3 input e calcula o maior e menor valor digitado