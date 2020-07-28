sexo = str(input('informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('DADOS invalido pf informe seu sexo: [M/F] ')).strip().upper()[0]
print('sexo {} registado com sucesso'.format(sexo))

# pg que valida o input com a funcao wile enquando nao estiver em mf nao deixa
