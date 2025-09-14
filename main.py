import random


LINHAS = 5
COLUNAS = 6
NUM_MINAS = 3

def criar_matriz(linhas, colunas, valor='.'):
    return [[valor for _ in range(colunas)] for _ in range(linhas)]

def gerar_minas(tabuleiro, num_minas):
    minas = set()
    while len(minas) < num_minas:
        i = random.randint(0, LINHAS - 1)
        j = random.randint(0, COLUNAS - 1)
        minas.add((i, j))
    for (i, j) in minas:
        tabuleiro[i][j] = '*'
    return minas

def contar_minas(tabuleiro, x, y):
    if tabuleiro[x][y] == '*':
        return '*'
    cont = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0 <= i < LINHAS and 0 <= j < COLUNAS:
                if tabuleiro[i][j] == '*':
                    cont += 1
    return cont if cont > 0 else ' '

def preparar_tabuleiro(num_minas):
    tabuleiro = criar_matriz(LINHAS, COLUNAS)
    gerar_minas(tabuleiro, num_minas)
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if tabuleiro[i][j] != '*':
                tabuleiro[i][j] = contar_minas(tabuleiro, i, j)
    return tabuleiro


def mostrar_tabuleiro(mat):
    print("   " + " ".join(str(i) for i in range(COLUNAS)))
    for i in range(LINHAS):
        linha = mat[i]
        print(f"{i:2} " + " ".join(str(c) for c in linha))

def revelar(tabuleiro, visivel, x, y):
    if visivel[x][y] != '.':
        return
    visivel[x][y] = tabuleiro[x][y]
    if tabuleiro[x][y] == ' ':
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if 0 <= i < LINHAS and 0 <= j < COLUNAS:
                    if visivel[i][j] == '.':
                        revelar(tabuleiro, visivel, i, j)

def venceu(tabuleiro, visivel):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if tabuleiro[i][j] != '*' and visivel[i][j] == '.':
                return False
    return True

def jogar():
    tabuleiro = preparar_tabuleiro(NUM_MINAS)
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

        if tabuleiro[x][y] == '*':
            print("BOOM! Você perdeu!")

            break
        revelar(tabuleiro, visivel, x, y)
        if venceu(tabuleiro, visivel):
            print("Parabéns! Você venceu!")
            mostrar_tabuleiro(tabuleiro)
            break

if __name__ == "__main__":
    jogar()
