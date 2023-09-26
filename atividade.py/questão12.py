numero_aluno = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_exercicios = float(input("Digite a média dos exercícios: "))
media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7
if media_aproveitamento >= 9.0:
    conceito = "A"
    print ("aprovado")
elif media_aproveitamento >= 7.5:
    conceito = "B"
    print ("aprovado")
elif media_aproveitamento >= 6.0:
    conceito = "C"
    print ("aprovado")
elif media_aproveitamento >= 4.0:
    conceito = "D"
    print ("reprovado")
else:
    conceito = "E"
    print ("reprovado")
print (media_aproveitamento)