fraze = str(input('digita uma frase ')).upper().strip()
print('esta fraze tem  um A na {} primeira posisao'.format(fraze.find('A')+1))
print('a ultima letra A aparece na {} posisao'.format(fraze.rfind('A')+1))
print('e ao todo esta fraze tem {} A '.format(fraze.count('A')))

#pg que analiza uma fraze e a letra em determinado posisao nesta foi a letra a