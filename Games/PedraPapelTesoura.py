import random

# Inicia o placar
vitorias = 0
derrotas = 0
empates = 0
rodada = 1

print("Bem-vindo ao Pedra, Papel e Tesoura INFINITO!")

while True:
    print(f"\nRodada {rodada}")
    print("Escolha: \n1 - Pedra\n2 - Papel\n3 - Tesoura\n4 - Sair")
    
    # Valida a jogada do usuário
    try:
        jogador = int(input("Sua jogada: "))
    except ValueError:
        print("Digite um número entre 1 e 4!")
        continue
    
    if jogador == 4:
        print("Até logo! 👋")
        break
    elif jogador not in [1, 2, 3]:
        print("Opção inválida! Tente 1, 2, 3 ou 4.")
        continue
    
    # Jogada do computador
    computador = random.randint(1, 3)
    opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
    
    print(f"\nVocê: {opcoes[jogador]}")
    print(f"Computador: {opcoes[computador]}")
    
    # Lógica do jogo
    if jogador == computador:
        print("Empate! 😊")
        empates += 1
    elif (jogador == 1 and computador == 3) or \
         (jogador == 2 and computador == 1) or \
         (jogador == 3 and computador == 2):
        print("Você ganhou! 🎉")
        vitorias += 1
    else:
        print("Computador ganhou! 💻")
        derrotas += 1
    
    # Atualiza e mostra o placar
    rodada += 1
    print(f"Placar: Você {vitorias} x {derrotas} Computador | Empates: {empates}")