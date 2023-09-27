salario = float(input("digite seu salário:"))
if salario <= 1903.98:
    imposto_de_renda = 0
elif salario <= 2826.65:
    imposto_de_renda = (salario - 1903.98) * 0.075
elif salario <= 3751.05:
    imposto_de_renda = (salario - 2826.65) * 0.15 + 142.80
elif salario <= 4664.68:
    imposto_de_renda = (salario - 2826.65) * 0.225 + 354.80
else:
    imposto_de_renda = (salario -4664.68) * 0,275 + 869.36
salario_liquido = salario - imposto_de_renda
print (f"salario liquido: RS {salario_liquido:2f}")
