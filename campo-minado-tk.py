import tkinter as tk
from tkinter import messagebox
import random


class CampoMinado:
    def __init__(self, root, linhas, colunas, minas):
        self.root = root
        self.linhas = linhas
        self.colunas = colunas
        self.minas = minas

        self.criar_tabuleiro()
        self.colocar_minas()
        self.criar_interface()

    def criar_tabuleiro(self):
        self.tabuleiro = [
            [" " for _ in range(self.colunas)] for _ in range(self.linhas)
        ]

    def colocar_minas(self):
        for _ in range(self.minas):
            while True:
                linha = random.randint(0, self.linhas - 1)
                coluna = random.randint(0, self.colunas - 1)
                if self.tabuleiro[linha][coluna] != "*":
                    self.tabuleiro[linha][coluna] = "*"
                    break

    def contar_minas_adjacentes(self, linha, coluna):
        contagem = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nova_linha, nova_coluna = linha + i, coluna + j
                if (
                    0 <= nova_linha < self.linhas
                    and 0 <= nova_coluna < self.colunas
                    and self.tabuleiro[nova_linha][nova_coluna] == "*"
                ):
                    contagem += 1
        return contagem

    def criar_interface(self):
        self.botoes = [[None] * self.colunas for _ in range(self.linhas)]

        for i in range(self.linhas):
            for j in range(self.colunas):
                self.botoes[i][j] = tk.Button(
                    self.root,
                    text="",
                    width=2,
                    height=1,
                    command=lambda i=i, j=j: self.clicar(i, j),
                )
                self.botoes[i][j].grid(row=i, column=j)

    def clicar(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == "*":
            self.revelar_todas_minas()
            messagebox.showinfo("Fim do Jogo", "Você atingiu uma mina! Fim do jogo.")
            self.root.quit()
        else:
            minas_adjacentes = self.contar_minas_adjacentes(linha, coluna)
            self.tabuleiro[linha][coluna] = str(minas_adjacentes)
            self.botoes[linha][coluna]["text"] = str(minas_adjacentes)
            if minas_adjacentes == 0:
                self.revelar_vizinhanca(linha, coluna)
            if self.verificar_vitoria():
                messagebox.showinfo("Parabéns!", "Você venceu!")
                self.root.quit()

    def revelar_vizinhanca(self, linha, coluna):
        for i in range(-1, 2):
            for j in range(-1, 2):
                nova_linha, nova_coluna = linha + i, coluna + j
                if 0 <= nova_linha < self.linhas and 0 <= nova_coluna < self.colunas:
                    if self.tabuleiro[nova_linha][nova_coluna] == " ":
                        minas_adjacentes = self.contar_minas_adjacentes(
                            nova_linha, nova_coluna
                        )
                        self.tabuleiro[nova_linha][nova_coluna] = str(minas_adjacentes)
                        self.botoes[nova_linha][nova_coluna]["text"] = str(
                            minas_adjacentes
                        )
                        if minas_adjacentes == 0:
                            self.revelar_vizinhanca(nova_linha, nova_coluna)

    def revelar_todas_minas(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.tabuleiro[i][j] == "*":
                    self.botoes[i][j]["text"] = "*"

    def verificar_vitoria(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.tabuleiro[i][j] != "*" and self.botoes[i][j]["text"] == "":
                    return False
        return True


def iniciar_jogo():
    # linhas = int(input("Número de linhas: "))
    # colunas = int(input("Número de colunas: "))
    # minas = int(input("Número de minas: "))
    linhas = 10
    colunas = 10
    minas = 10
    root = tk.Tk()
    root.title("Campo Minado")

    campo_minado = CampoMinado(root, linhas, colunas, minas)

    root.mainloop()


if __name__ == "__main__":
    iniciar_jogo()
