preco_etiqueta = float(input("Digite o preço da etiqueta: RS "))
codigo_condicao = int(input("Digite o seu código da condição de pagamento (1, 2, 3 ou 4): "))
if codigo_condicao == 1: 
    valor_pago = preco_etiqueta - (preco_etiqueta * 0.10)
elif codigo_condicao == 2:
    valor_pago = preco_etiqueta - (preco_etiqueta * 0.15)
elif codigo_condicao == 3:
    valor_pago = preco_etiqueta
elif codigo_condicao == 4:
    valor_pago = preco_etiqueta + (preco_etiqueta * 0.10)
print (valor_pago)

 