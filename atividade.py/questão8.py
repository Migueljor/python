valor1 = int(input("digite seu primeiro valor inteiro:"))
valor2 = int(input("digite seu segundo valor inteiro:"))
valor3 = int(input("digite seu terceiro valor inteiro:"))
maior = max(valor1, valor2, valor3)
menor = min(valor1, valor2, valor3)
medio = valor1 + valor2 + valor3 - maior - menor
print("valores em ordem decrescente:", maior, medio, menor)
