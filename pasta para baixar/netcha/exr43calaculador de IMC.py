peso = float(input('qual é o seu peso? '))
altura = float(input('qual é a sua altura? '))
imc = peso /(altura ** 2)
print('o IMC  dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso.')
elif 18.5 <= imc < 25:
    print('parabens voce esta com o peso normal.')
elif 25 <= imc < 30:
    print('voce esta em Sobrepeso:')
elif 30 <= imc < 40:
    print('Cuidado voce esta obesa.')
else:
    print('voce acima do obeso tem que ir ao hospital.')

# pg que calcula o imc de uma pessao mais uma vez if e elif