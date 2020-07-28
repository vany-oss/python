print('analizador de triangolo')
r1 = float(input('1 seguimento '))
r2 = float(input('2 seguimento '))
r3 = float(input('3 seguimento '))
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
	print('os seguimentos Podem Formar triangolo')
else:
	print('os seguimentos nao podem formar triangolo')
	
# lpg que calcula os seguimentos de triangolo
