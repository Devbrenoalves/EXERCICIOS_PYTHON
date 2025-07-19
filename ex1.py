#Faça um Programa que peça dois números e imprima o maior deles.
try:
    numero1 = int(input('Digite o 1 numero'))
    numero2 = int(input('Digite o 2 numero'))

    if numero1 > numero2:
        print(numero1, ' é maior')
    else:
        print(numero2, ' é maior')

except ValueError:
    print('Por favor, digite números válidos.')
except Exception as e:
    print('Ocorreu um erro:', e)