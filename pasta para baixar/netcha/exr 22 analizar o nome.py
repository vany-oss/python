nome = str(input('seu nome completo? ')).strip()
print(' seu nome em maiuscula é {} '.format(nome.upper()))
print('seu  nome em minucule é {} '.format(nome.lower()))
print('o seu nome tem {}'.format(len(nome) - nome.count(' ')))
print('o seu primeiro nome tem {}'.format(nome.find(' ')))

# pg que analiza o seu nome completo por M m e tamaio de letras. tambem podia se ultilizar o split para a contagem da letra do primeiro nome