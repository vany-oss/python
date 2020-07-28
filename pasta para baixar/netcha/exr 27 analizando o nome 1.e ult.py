n = str(input('seu nome completo ')).strip()
nome = n.split()
prnt('prazer em te conhecer')
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))

#pg que analiza o primeiro e ultimo nome fazendo a fateamento para saber o ultimo nome e fazer o len aucontrario - e é usa a funcao split para factear