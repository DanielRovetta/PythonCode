import random


def criar_tabuleiro(linhas, colunas, minas):
    tabuleiro = [[" " for _ in range(colunas)] for _ in range(linhas)]

    # Colocar minas aleatórias no tabuleiro
    for _ in range(minas):
        while True:
            linha = random.randint(0, linhas - 1)
            coluna = random.randint(0, colunas - 1)
            if tabuleiro[linha][coluna] != "*":
                tabuleiro[linha][coluna] = "*"
                break

    return tabuleiro


def imprimir_tabuleiro(tabuleiro, mostrar_minas=False):
    for linha in tabuleiro:
        for celula in linha:
            if celula == "*" and not mostrar_minas:
                print(" ", end=" ")
            else:
                print(celula, end=" ")
        print()


def contar_minas_adjacentes(tabuleiro, linha, coluna):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])
    contagem = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            nova_linha, nova_coluna = linha + i, coluna + j
            if (
                0 <= nova_linha < linhas
                and 0 <= nova_coluna < colunas
                and tabuleiro[nova_linha][nova_coluna] == "*"
            ):
                contagem += 1

    return contagem


def revelar_vizinhanca(tabuleiro, tabuleiro_exibicao, linha, coluna):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])

    # Se a célula já foi revelada ou é uma mina, pare
    if tabuleiro_exibicao[linha][coluna] != " " or tabuleiro[linha][coluna] == "*":
        return

    # Contar minas adjacentes
    minas_adjacentes = contar_minas_adjacentes(tabuleiro, linha, coluna)
    tabuleiro_exibicao[linha][coluna] = str(minas_adjacentes)

    # Se não há minas adjacentes, revelar a vizinhança recursivamente
    if minas_adjacentes == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                nova_linha, nova_coluna = linha + i, coluna + j
                if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas:
                    revelar_vizinhanca(
                        tabuleiro, tabuleiro_exibicao, nova_linha, nova_coluna
                    )


def jogar():
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))
    minas = int(input("Número de minas: "))

    tabuleiro = criar_tabuleiro(linhas, colunas, minas)
    tabuleiro_exibicao = [[" " for _ in range(colunas)] for _ in range(linhas)]

    while True:
        imprimir_tabuleiro(tabuleiro_exibicao)

        linha = int(input("Digite a linha (0 a {}): ".format(linhas - 1)))
        coluna = int(input("Digite a coluna (0 a {}): ".format(colunas - 1)))

        if tabuleiro[linha][coluna] == "*":
            print("Você atingiu uma mina! Fim do jogo.")
            imprimir_tabuleiro(tabuleiro, mostrar_minas=True)
            break
        else:
            revelar_vizinhanca(tabuleiro, tabuleiro_exibicao, linha, coluna)

        if all(
            tabuleiro_exibicao[i][j] != " " or tabuleiro[i][j] == "*"
            for i in range(linhas)
            for j in range(colunas)
        ):
            print("Parabéns! Você ganhou!")
            imprimir_tabuleiro(tabuleiro, mostrar_minas=True)
            break


if __name__ == "__main__":
    jogar()
