from datetime import date 
ac = date.today().year
tmaior = 0
tmenor =0
for pes in range(1, 8):
	nasc = int(input('ano da {}° pessoa? '.format(pes)))
	idade = ac - nasc
	if idade >= 18:
		tmaior += 1
	else:
		tmenor +=1 
print(f'ao todo tivemos {tmaior} pessoas maior de idade')
print(f'e tevemos {tmenor} pesoas menores de idade')