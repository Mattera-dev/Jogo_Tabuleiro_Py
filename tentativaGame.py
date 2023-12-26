import random
from MyClasses import player, tabuleiro

tamanho = input("Digite o tamanho do tabuleiro (siga o exemplo: '5x5' '4x6') :").split('x')
tesouro = [(random.randint(1,(int(tamanho[0]) - 1))), (random.randint(0,int(tamanho[1]) - 1))]
tabu = tabuleiro(int(tamanho[0]), int(tamanho[1]))
p1 = player([0,0], 0, int(tamanho[0]), int(tamanho[1]))
minMoves = p1.posi[0] + tesouro[0] + p1.posi[1] + tesouro[1]

def checarWin():
    if p1.posi == tesouro:
        print("Voce ganhou!")
        print(f'Voce usou um total de {p1.moves} Movimentos')
        return True
    return False

def showtabu():
    tabu.gerarTabuleiro(p1.posi, tesouro)
    print("Movimentos atuais: ", p1.moves)
    print("Movimentos minimos para ganhar: ", minMoves)
    move =  input('\n\nDigite o seu movimento como a um jogo normal "WASD" :')
    print("\033c")
    if p1.mover(move) != 1:
        print(p1.mover(move))
        
while not checarWin():
        showtabu()




