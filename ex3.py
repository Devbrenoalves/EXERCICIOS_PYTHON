#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = (input('Qual seu sexo? [F ou M]'))

if (sexo == 'F'):
    print('é muié')
elif (sexo == 'M'):
    print('É HOMI')
else:
    print('É VIADO')