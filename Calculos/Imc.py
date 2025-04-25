#variavies
nome =  (input("Digite seu nome: "))
peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))


#calculoDoProjeto
imc = peso / (altura ** 2)




#exibirPesoIdeal
print(f"{nome} seu peso ideal é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Magreza")
elif 18.5 <= imc < 25:
    print("Classificação: Normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 40:
    print("Classificação: Obesidade")
else:
    print("Classificação: Obesidade Grav")
