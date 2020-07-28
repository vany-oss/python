salario = float(input('qual é o salario?'))
if salario <= 1250:
	nsal = salario + (salario* 15 /100)
else:
	 nsal = salario + (salario * 10 /100)
print(f'quem ganhava {salario} euros  agora ganha {nsal} euros')

#pg que calcula um aumentob de  de salario se o salario foir maior que 1250 tem um aumento de 10% senao tera um aumento de 15 %
