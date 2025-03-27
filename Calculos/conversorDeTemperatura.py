# Conversor de Temperatura (Celsius ↔ Fahrenheit)
print("Escolha a conversão:")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
opcao = input("Digite 1 ou 2: ")

if opcao == "1":
    # Conversão Celsius → Fahrenheit
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32  # Fórmula
    print(f"\n{celsius:.1f}°C equivalem a {fahrenheit:.1f}°F")
elif opcao == "2":
    # Conversão Fahrenheit → Celsius
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9  # Fórmula
    print(f"\n{fahrenheit:.1f}°F equivalem a {celsius:.1f}°C")
else:
    print("\nOpção inválida! Digite 1 ou 2.")