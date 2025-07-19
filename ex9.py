# Lê três números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Coloca os números em uma lista e ordena em ordem decrescente
numeros = [num1, num2, num3]
numeros.sort(reverse=True)

# Mostra os números em ordem decrescente
print("Números em ordem decrescente:", numeros)