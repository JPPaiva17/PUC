from random import choices

def simulador(nRodadas, quantia, probabilidade):
    nJogadores = len(quantia)
    jogadores = list(range(nJogadores))
    quantiaFinal = quantia
    rodada = 0

    while((rodada < nRodadas) and (min(quantiaFinal) > 0)):
        rodada +=1
        quantiaFinal = [q - 1 for q in quantiaFinal]
        vencedor = choices(jogadores, weights = probabilidade)[0]
        quantiaFinal[vencedor] += nJogadores
    
    return quantiaFinal


numeroRodadas = 1000
quantiaInicial = [150, 70, 240]
probabilidadeVencer = [0.3, 0.4, 0.3]
campeonato = simulador(numeroRodadas, quantiaInicial, probabilidadeVencer)

print("Quantia Final")
print(f"Maria = {campeonato[0]}")
print(f"Gustavo = {campeonato[1]}")
print(f"Jorge = {campeonato[2]}")
