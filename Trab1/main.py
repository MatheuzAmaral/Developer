#variavéis
Nota1 = float(input("Digite a nota 1: "))
Nota2 = float(input("Digite a nota 2: " ))
Nota3 = float(input("Digite a nota 3: "))

#calculodoTrab1
media = (Nota1 + Nota2 + Nota3) / 3

#exibindo_Resultado
print(f"A média das notas é: {media:.1f}")


#Mensagens_mostrando_se_foi_aprovado_ou_reprovado
if media >= 7:
    print("Você foi aprovado")

else:
    print("Você foi reprovado")



