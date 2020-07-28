nata1 = float(input('primeira nota '))
nota2 = float(input('segunda nota '))
media = (nata1 + nota2) / 2
print('o aluno teve uma media de {} valor.'.format(media))
if media >= 9.5:
    print('o aluno esta APROVADO!')
elif media >= 9.3 and media < 9.4:
    print('o aluno vai a recuperacao.')
else:
    print('o aluno reprovou')

    #pg que aprova o aluno com algumas condiçẽs