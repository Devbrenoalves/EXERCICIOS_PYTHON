import math

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação: + para soma, - para subtração, * para multiplicação, / para divisão")
operacao = input("Operação: ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 == 0:
        print("Divisão por zero não é permitida.")
        exit()
    resultado = num1 / num2
else:
    print("Operação inválida.")
    exit()

print(f"Resultado da operação: {resultado}")

# Par ou ímpar
if resultado % 2 == 0:
    print("O resultado é par.")
else:
    print("O resultado é ímpar.")

# Positivo ou negativo
if resultado > 0:
    print("O resultado é positivo.")
elif resultado < 0:
    print("O resultado é negativo.")
else:
    print("O resultado é zero.")

# Inteiro ou decimal
if resultado == math.floor(resultado) or resultado == math.ceil(resultado):
    print("O resultado é inteiro.")
else:
    print("O resultado é decimal.")