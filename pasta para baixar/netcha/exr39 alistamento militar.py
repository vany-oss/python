from datetime import date
actual = date.today().year
nasc = int(input('ano do seu nascimento? '))
idade = actual - nasc
print('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, actual))
if idade == 18:
    print('voce tem que alistar IMIDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o seu alistamento'.format(saldo))
    ano = actual + saldo
    print('o seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('voce deveria alistar ha {} anos atras. '.format(saldo))
    ano = actual - saldo
    print('o seu alistamento foi no ano {}  '.format(ano))

# pg que analiza o ano do seu nascimento e diz quando vais para a tropa quando deverias ir e quando
#será



