somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelh = 0
totalmulher20 = 0
for p in range(1, 5):
    print('------- {}º PESSOA ------'.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F] ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem += idade
        nomevelh = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelh = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print('a media de idade de grupo é de {} anos'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelh))
print('ao todo são {} mulheres co menos de 20anos'.format(totalmulher20))

#pg que analisa segunda idade sexo ainda apresenta o homem mais velho diz o nome dle e diz quantas mulheres temmenos de 20 annos