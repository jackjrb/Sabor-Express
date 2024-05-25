x = int(input('Digite a coordenada x:\n'))
y = int((input('Digite a coordenada y:\n')))

if x>0 and y>0:
    print('Você está no primeiro quadrante')
elif x<0 and y>0:
    print('Você está no segundo quadrante')
elif x<0 and y<0:
    print('Você está no terceiro quadrante')
elif x>0 and y<0:
    print('Você está no quarto quadrante')
else:
    print('Você está localizado no eixo ou origem')