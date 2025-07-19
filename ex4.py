#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Coloque sua letra: ').lower()

if len(letra) != 1 or not letra.isalpha():
    print('Por favor, digite apenas uma letra.')
elif letra in 'aeiou':
    print('É vogal')
else:
    print('Consoante')