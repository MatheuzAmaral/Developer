import random
import string

tamanho = int(input("Quantos caracteres terá a senha? (Ex: 8, 12): "))

# Caracteres possíveis (letras + números + símbolos)
caracteres = string.ascii_letters + string.digits + "!@#$%&*"

# Gera a senha aleatória
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print(f"\nSenha gerada: {senha}")