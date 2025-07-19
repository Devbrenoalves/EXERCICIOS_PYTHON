#Faça um Programa que leia três números e mostre o maior e o menor deles.
x = int(input('...'))
y = int(input('...'))
z = int(input('...'))

#MAIOR
if(x > y and x > z):
    maior = x
elif(y > x and y > z):
    maior = y
else:
    maior = z

#MENOR
if(x < y and x < z):
    menor = x
elif(y < x and y < z):
    menor = y
else:
    menor = z

print('O maior numero é o', maior, 'e o menor e o', menor)