import random
import time

# Função para escolher número de jogadores e dificuldade com validação
def escolher_opcao(mensagem, opcoes_validas):
    while True:
        try:
            opcao = int(input(mensagem))
            if opcao in opcoes_validas:
                return opcao
            else:
                print(f"Erro: escolha uma das opções válidas: {opcoes_validas}")
        except ValueError:
            print("Erro: Digite um número válido.")

# Função para gerar números de acordo com a dificuldade
def gerar_numeros(dificuldade):
    if dificuldade == 3:
        return random.randint(-10, 10), random.randint(-10, 10)
    elif dificuldade == 4:
        return random.randint(-100, 100), random.randint(-100, 100)
    elif dificuldade == 5:
        return random.randint(-1000, 1000), random.randint(-1000, 1000)

# Função para realizar uma operação matemática com tempo de execução
def realizar_operacao(operacao, numero_1, numero_2, ponto_atual):
    print(f"{numero_1} {operacao} {numero_2} = ?")
    resultado_correto = eval(f"{numero_1} {operacao} {numero_2}")
    tempo_inicio = time.time()
    try:
        resposta = int(input("Digite sua resposta: "))
    except ValueError:
        print("Erro: Digite um número válido.")
        return ponto_atual  # Não altera pontuação
    tempo_exec = time.time() - tempo_inicio
    print(f"Tempo de execução: {tempo_exec:.2f} segundos")

    if tempo_exec > 30:
        return ponto_atual
    elif resposta == resultado_correto:
        if tempo_exec <= 5:
            return ponto_atual + 10
        else:
            return ponto_atual + max(0, 10 - (tempo_exec - 5) * 0.2)
    return ponto_atual

# Função para um turno de jogo
def jogar_turno(ponto_atual, dificuldade):
    operacoes = ['+', '-', '*', '//']
    for operacao in operacoes:
        numero_1, numero_2 = gerar_numeros(dificuldade)
        ponto_atual = realizar_operacao(operacao, numero_1, numero_2, ponto_atual)
        print(f"Pontuação atual: {ponto_atual}\n")
    return ponto_atual

# Jogo principal
print("1 - Individual\n2 - Dupla")
numero_jogadores = escolher_opcao("Escolha o número de jogadores: ", [1, 2])
print("\n3 - Fácil\n4 - Médio\n5 - Difícil")
dificuldade = escolher_opcao("Escolha a dificuldade: ", [3, 4, 5])

# Jogo para um ou dois jogadores
pontos_jogador_1 = jogar_turno(0, dificuldade)
if numero_jogadores == 2:
    print("\nJogador 2:")
    pontos_jogador_2 = jogar_turno(0, dificuldade)
    if pontos_jogador_1 > pontos_jogador_2:
        print("Jogador 1 ganhou!")
    elif pontos_jogador_1 < pontos_jogador_2:
        print("Jogador 2 ganhou!")
    else:
        print("Empate!")
else:
    print(f"Sua pontuação final foi: {pontos_jogador_1}")

print("Fim de jogo!")