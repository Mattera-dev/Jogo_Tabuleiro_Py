import random


class player:
    def __init__(self, posi, moves, maxmoveX, maxmoveY):
        self.posi = posi
        self.moves = moves
        self.maxmoveX = maxmoveX
        self.maxmoveY = maxmoveY

    def mover(self, move):
        if move.lower() == 'w':
            if self.posi[0] > 0:
                self.moves += 1
                self.posi[0] -= 1
                return 1
            else:
                return "Voce esta na beirada do tabuleiro faca outro movimento!"
        if move.lower() == 's':
            if self.posi[0] < self.maxmoveY-1:
                self.moves += 1
                self.posi[0] += 1
                return 1
            else:
                return "Voce esta na beirada do tabuleiro faca outro movimento!"
        if move.lower() == 'a':
            if self.posi[1] > 0:
                self.moves += 1
                self.posi[1] -= 1
                return 1
            else:
                return "Voce esta na beirada do tabuleiro faca outro movimento!"
        if move.lower() == 'd':
            if self.posi[1] < self.maxmoveX-1:
                self.moves += 1
                self.posi[1] += 1
                return 1
            else:
                return "Voce esta na beirada do tabuleiro faca outro movimento!"
        if move != 'a' and move != 's' and move != 'w' and move != 'd':
            return "selecione uma opcao valida"


class tabuleiro:
    def __init__(self, larg, alt):
        self.larg = larg
        self.alt = alt

    def gerarTabuleiro(self, playPos, treaPos):
        aux = []
        for linha in range(0, self.alt):
            for coluna in range(0, self.larg):
                if linha == playPos[0] and coluna == playPos[1]:
                    aux += 'V'
                elif linha == treaPos[0] and coluna == treaPos[1]:
                    aux += 'T'
                else:
                    aux += '+'
            aux += '\n'
        for i in aux:
            print(' ' + i, end='')
        return aux
