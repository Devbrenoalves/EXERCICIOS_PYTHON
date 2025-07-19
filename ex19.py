numero = int(input("Digite um número inteiro menor que 1000: "))

if numero < 0 or numero >= 1000:
    print("Número inválido. Deve ser entre 0 e 999.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas > 0:
        partes.append(f"{centenas} centena{'s' if centenas > 1 else ''}")
    if dezenas > 0:
        partes.append(f"{dezenas} dezena{'s' if dezenas > 1 else ''}")
    if unidades > 0:
        partes.append(f"{unidades} unidade{'s' if unidades > 1 else ''}")

    if not partes:
        print("0 unidade")
    elif len(partes) == 1:
        print(partes[0])
    elif len(partes) == 2:
        print(f"{partes[0]} e {partes[1]}")
    else:
        print(f"{partes[0]}, {partes[1]} e {partes[2]}")