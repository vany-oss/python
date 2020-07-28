csa = float(input('qual é o valor da casa? '))
sala = float(input('qual é o salario? '))
anos = int(input('em quantos anos? '))
prest = csa / (anos * 12)
min = sala * 30 /100
print('para pagar uma casa  {:.2f} euros em {} anos'.format(csa, anos))
print('a prestacao sera de {:.2f} euros mensal'.format(prest))
if  prest <= min:
 	print('Emprestimo pode ser aprovado')
else:
 	print('Infilismente o eprestimo é negado')
 	
 # pg que calcula emprestimo da casa nap ecendendo 30% de salario do comprador