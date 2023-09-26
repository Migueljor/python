altura = float(input("digite sua altura (em metros):"))
sexo = input("digite seu sexo (M para masculino, F para feminino: ")
if sexo == "M":
    melhor_peso = (72.7 * altura) -58
elif sexo == "F":
    melhor_peso = (62.1 * altura) - 44.7
else:
    print("não identificado")

print("peso ideal:", melhor_peso, "quilogramas")