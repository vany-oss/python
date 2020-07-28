velo = float(input('velocidade actual? '))
if velo > 80:
	print('multado voce esxcedeu o limitite permitido')
	multa = (velo -80 ) * 0.50
	print('voce deve pagar a multa de {} euros'.format(multa))
	
print('bom dia faca uma boa conducao')
# pg que calcula a multa d caro se a velocidade permida for escnxcedida o valor da multae 0.50 claro que se podia utilizar else mas e uma condicao simples 