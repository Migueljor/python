peso = float(input("Digite o peso em (em kg): "))
altura = float(input("Digite a altura(em metros): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    condicao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    condicao = "normal"
elif 25 <= imc < 30:
    condicao = "Acima do peso"
else:
    condicao = "Obeso"
print("IMC:", imc)
print("Condição:", condicao)