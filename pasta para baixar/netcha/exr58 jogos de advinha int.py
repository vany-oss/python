#Eu Fiz uma coisa assim, com a tua ajuda prof: na verdade eu queria que o gamel avisasse só uma vez, k ele começa a ganhar 2 euros,mas vi que fica mais dificil para o jogadr, pk jà o gamel deixou de dar palpites..

from random import randint
gamel = randint(0, 20)
print ('=-=' * 20)
print( 'Sou Gamel acabei de pensar em um Nr entre 0 a 20:\n\033[32mDOU 4 PALPITES\033[m:')
print('Tens 20 Euros para Iniciar:')
print('Se ganhares à Primeira Recebes\nO Dóbro 44 euros.\nAté 3* Tentativas Mesmo Erada Ganhas 2$: \033[33m(4 $ é bonos..)\033[m\nMas apartir da 3* tentativa  erada\nEu Ganho 2 Euros, por cada Resposta que eraste. TOPAS ?\nSe Sim ')
print ('Tenta Advinhar :')
print ('=-=' * 20)
acertou = False
tentativa = 0
ponto = 20
ganhoeu = 0
while not acertou:
	j = int(input ('Qual é o teu palpite ? -->'))
	tentativa = tentativa + 1
	ponto = ponto -2
	ganhoeu =  2* tentativa - 6
	if j == gamel: 
		acertou = True
	elif tentativa >= 4:
         print ('\033[32mATENÇÃO! AGORA COMEÇO A GANHAR 2 EUROS:\nPOR CADA ERRO TEU: \033[31mCUIDADO JÁ SÓ TENS {}  Euros\n\033[33mAgora vai ficar mais Dificil.\n\033[44mNa verdade é Só Prestares Atenção.\033[m'.format(ponto + 6))
	else:
			if j < gamel:
				print ('É Mais --> tente outra vez')
			elif j  >  gamel:
		   	       print ('É Menos --> tente outra vez')

	       
print ('voce acertou em {} tentativas \033[35me ficaste com {}\033[m euros.'.format(tentativa, ponto +6  ))
print('\033[31mEu Ganhei {}\033[m Euros.'.format(ganhoeu ))
print ('Autor Vany')