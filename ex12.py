valor_hora = float(input("Digite o valor da sua hora: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

# Cálculo do IR
if salario_bruto <= 900:
    ir_percentual = 0
elif salario_bruto <= 1500:
    ir_percentual = 5
elif salario_bruto <= 2500:
    ir_percentual = 10
else:
    ir_percentual = 20

ir = salario_bruto * ir_percentual / 100
inss = salario_bruto * 10 / 100
sindicato = salario_bruto * 3 / 100
fgts = salario_bruto * 11 / 100

total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_percentual}%) : R$ {ir:.2f}")
print(f"(-) INSS (10%) : R$ {inss:.2f}")
print(f"(-) Sindicato (3%) : R$ {sindicato:.2f}")
print(f"FGTS (11%) : R$ {fgts:.2f}")
print(f"Total de descontos : R$ {total_descontos:.2f}")
print(f"Salário Líquido :R$ {salario_liquido:.2f}")
