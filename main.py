import random
import numpy as np

LINHAS = 1
COLUNAS = 1
MINAS = 1

with open("cfg.txt", 'r') as f:
    conteudo = f.readlines()
    i = 0
    while (i < len(conteudo)):
        conteudo[i] = conteudo[i].strip().split('=')
        match conteudo[i][0]:
            case 'LINHAS':
                LINHAS = int(conteudo[i][1])
            case 'COLUNAS':
                COLUNAS = int(conteudo[i][1])
            case 'MINAS':
                MINAS = int(conteudo[i][1])
        i += 1


def criar_matriz(linhas, colunas, valor='.'):
    return np.full((linhas, colunas), valor, dtype=str)


def gerar_minas(tabuleiro, qtd_minas):
    posicoes = set()
    while len(posicoes) < qtd_minas:
        i = random.randint(0, LINHAS - 1)
        j = random.randint(0, COLUNAS - 1)
        posicoes.add((i, j))
    for (i, j) in posicoes:
        tabuleiro[i, j] = '*'
    return posicoes


def contar_minas(tabuleiro, x, y):
    if tabuleiro[x, y] == '*':
        return '*'
    cont = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0 <= i < LINHAS and 0 <= j < COLUNAS:
                if tabuleiro[i, j] == '*':
                    cont += 1
    return str(cont) if cont > 0 else '#'


def preparar_tabuleiro(minas):
    tabuleiro = criar_matriz(LINHAS, COLUNAS)
    gerar_minas(tabuleiro, minas)
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if tabuleiro[i, j] != '*':
                tabuleiro[i, j] = contar_minas(tabuleiro, i, j)
    return tabuleiro


def mostrar_tabuleiro(mat):
    print("   " + " ".join(str(i) for i in range(COLUNAS)))
    for i in range(LINHAS):
        linha = mat[i]
        print(f"{i:2} " + " ".join(linha))


def revelar(tabuleiro, visivel, x, y):
    if visivel[x, y] != '.':
        return
    visivel[x, y] = tabuleiro[x, y]
    if tabuleiro[x, y] == '#':
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if 0 <= i < LINHAS and 0 <= j < COLUNAS:
                    if visivel[i, j] == '.':
                        revelar(tabuleiro, visivel, i, j)


def venceu(tabuleiro, visivel):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if tabuleiro[i, j] != '*' and visivel[i, j] == '.':
                return False
    return True


def jogar():
    tabuleiro = preparar_tabuleiro(MINAS)
    visivel = criar_matriz(LINHAS, COLUNAS)
    while True:
        mostrar_tabuleiro(visivel)
        try:
            x = int(input("Linha: "))
            y = int(input("Coluna: "))
        except ValueError:
            print("Digite números válidos!")
            continue

        if not (0 <= x < LINHAS and 0 <= y < COLUNAS):
            print("Coordenadas fora do tabuleiro!")
            continue

        if tabuleiro[x, y] == '*':
            print("BOOM! Você perdeu!")
            break
        revelar(tabuleiro, visivel, x, y)
        if venceu(tabuleiro, visivel):
            print("Parabéns! Você venceu!")
            mostrar_tabuleiro(tabuleiro)
            break


if __name__ == "__main__":
    jogar()
