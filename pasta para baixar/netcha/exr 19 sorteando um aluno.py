from random import choice
n = str(input('primeiro aluno '))
n1 = str(input('segundo aluno '))
n2= str(input('terceiro aluno '))
n3 = str(input('quarto aluno '))
lista = [n, n1, n2, n3, ]
esc = choice(lista)
print(f' o aluno sorteado é {esc}')

# pg que sortea aluno ou algo de uma forma aleotoria e escolhido, e obvido que dava para a maquina burlar mas por enquanto fica assim e tambem para emparalhar era so usar shuffle 