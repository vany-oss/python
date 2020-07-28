from datetime import date
actual = date.today().year
nasc = int(input('Data do seu nascimento '))
idade = actual - nasc
print(f'O ateleta tem {idade} anos.')
if idade <= 9:
    print('Classificaçao: Mirim.')
elif idade  <= 15:
    print('Classificação Infantil.')
elif idade <= 19:
    print('Classificação Junior.')
elif idade <= 25:
    print('Classificação Senior.')
else:
    print('Classificação Master.')

#pg que classifica os ateleta conforme a sua idade usanda if e el 5 veses