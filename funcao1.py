def somar(a, b):
    print("Resultado da soma", a+b)

def subtrair(a, b):
    print("Resultado da subtração", a-b)

def multiplicar(a, b):
    print("Resultado da multiplicação", a*b)

def dividir(a, b):
    if b == 0:
        print("Divisão por zero não é permitida.")
    else:
        print("Resultado da divisão", a/b)

# chamada da função
somar(3, 4)
subtrair(10, 5)
multiplicar(2, 3)
dividir(8, 2)