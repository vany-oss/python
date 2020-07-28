dist = float(input('qual e a distantancia? '))
if dist >= 100:
	pre = dist * 0.50
else:
	pre=n = dist * 0.35
print('esta a fazer uma viagem de {}km tem que pagar {:.2f} euros'.format(dist, pre))

# pg k calcula o preco da viagem por km e apartir de 100 km reduz de preco conforme a variavel o preco inicial era de 0.50 cetimo pr km e dpois e 0.35