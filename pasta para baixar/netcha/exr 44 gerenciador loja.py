print('=+=' * 20)
print('{:=^40}'.format(' Loga Netcha '))
print('=+=' * 20)
#print('se pagar tudo hoje com dinheiro /cheque tem 10% Desconto\nse pagar com cartao hoje tudo 5% de desconto')
#print('se pagar 2x no cartao preço normal\nse pagar 3x no cartao ou mais 20% de Juros')
preço = float(input('qual é o preço? '))
print('''FORMAS DE PAGAMENTO
[ 1 ] Pronto á dinheiro/cheque 10% Desconto
[ 2 ] pronto com cartao 5% Desconto
[ 3 ] 2x no cartao sem juros
[ 4 ] 3x ou mais com cartão com juros''')
op = int(input('qual é a sua opção? '))
if op == 1:
    total = preço - (preço * 10 / 100)
elif op == 2:
    total = preço - (preço * 5 / 100)
elif op == 3:
    total = preço
    parcela = total / 2
    print('a sua compra sera paga em 2x de {} euros SEM JUROS'.format(parcela))
elif op == 4:
    total = preço + (preço * 20 / 100)
    toparc = int(input('em quantas vezes? '))
    parcela = total /toparc
    print('o seu pagamento sera dividido em {}x de {:.2f} euros com Juros'.format(toparc, parcela))
else:
    total = preço
    print('Opcao Invalida tente novamente.')
print('sua compra de {:.2f} euros vai ficar {:.2f} euros no Final'.format(preço, total))

# pg que calcula o preço e o pagamento sao formas de pagamentos nao é um sistema da loga e so de pagamento
# com algumas opçãos de pagamentos.



