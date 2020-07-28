n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa ''')
    op = int(input('qual é a sua opção? '))
    if op == 1:
        soma  = n1 + n2
        print(f'a soma entre {n1} e {n2} é {soma}')
    elif op == 2:
        prod = n1 * n2
        print(f'multiplicando os dois valores temos {prod}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maio valor é {}'.format(n1, n2 , maior))
    elif op == 4:
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif op == 5:
        print('finalizando...')
    else:
        print('opção invalida tente novamente')
    print('=-=' *10)


print('Fim  do programa volte sempre')

#pg de menu com opçpoes