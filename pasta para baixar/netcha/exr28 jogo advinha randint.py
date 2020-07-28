from random import randint
cp = randint(0, 5)
print('=+=' * 20)
print('vou pensar em um nr entre 0 a 5 tente advinhar! ')
print('=+' *20)
jd = int(input('da o seu palpite '))
if jd == cp:
	print('parabens voce me ganhau')
else:
	print('ganhaei pensei em nr {}'.format(cp))
	
#pg que joga com o usuario computador pensa 