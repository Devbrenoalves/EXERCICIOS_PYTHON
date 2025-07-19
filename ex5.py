#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

try:
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))

    if nota1 < 0 or nota2 < 0:
        print("Notas não podem ser negativas.")
    elif nota1 > 10 or nota2 > 10:
        print("Notas devem estar entre 0 e 10.")
    else:
        media = (nota1 + nota2) / 2
        print(f"Média: {media}")
        if media == 10:
            print("Aprovado com Distinção")
        elif media >= 7:
            print("Aprovado")
        elif media >= 5:
            print("Recuperação")
        else:
            print("Reprovado")

except ValueError:
    print("Por favor, digite números válidos.")
except Exception as e:
    print("Ocorreu um erro:", e) 