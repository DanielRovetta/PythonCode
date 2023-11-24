import tkinter as tk
from tkinter import *
import random
import copy


class Bloco:
    j: int
    i: int
    estado: str
    valor: int

    def __init__(self, j, i, valor, estado):
        self.j = j
        self.i = i
        self.valor = valor
        self.estado = estado


class Campo:
    def __init__(self, root, linhas, colunas):
        self.root = root
        self.linhas = linhas
        self.colunas = colunas

        self.criarCampo()

    def criarCampo(self):
        self.blocos = [[None] * self.colunas for _ in range(self.linhas)]

        for j in range(self.linhas):
            for i in range(self.colunas):
                bloco = Bloco(j, i, 0, "vazio")
                self.blocos[j][i] = bloco

    def gerarObstaculos(self):
        j = random.randint(0, self.linhas - 1)
        i = random.randint(0, self.colunas - 1)

        while self.blocos[j][i].estado != "vazio":
            j = random.randint(0, self.linhas - 1)
            i = random.randint(0, self.colunas - 1)

        self.blocos[j][i].valor = 0
        self.blocos[j][i].estado = "parede"

    def gerarInicio(self):
        j = random.randint(0, self.linhas - 1)
        i = random.randint(0, self.colunas - 1)

        while self.blocos[j][i].estado != "vazio":
            j = random.randint(0, self.linhas - 1)
            i = random.randint(0, self.colunas - 1)

        self.blocos[j][i].valor = 0
        self.blocos[j][i].estado = "inicio"
        self.blocos[j][i].j = j
        self.blocos[j][i].i = i

        self.inicio = self.blocos[j][i]

    def gerarFim(self):
        j = random.randint(0, self.linhas - 1)
        i = random.randint(0, self.colunas - 1)

        while self.blocos[j][i].estado != "vazio":
            j = random.randint(0, self.linhas - 1)
            i = random.randint(0, self.colunas - 1)

        self.blocos[j][i].valor = 0
        self.blocos[j][i].estado = "fim"
        self.blocos[j][i].j = j
        self.blocos[j][i].i = i

        self.fim = self.blocos[j][i]

    def criarInterface(self):
        campo = [[None] * self.colunas for _ in range(self.linhas)]
        for j in range(self.linhas):
            for i in range(self.colunas):
                bloco = tk.Label(
                    self.root,
                    width=5,
                    height=2,
                    text=self.blocos[j][i].valor,
                    bd=0.5,
                    relief="solid",
                    bg="white",
                )
                if self.blocos[j][i].estado == "vazio":
                    bloco.config(
                        bg="white",
                        fg="black",
                    )

                if self.blocos[j][i].estado == "inicio":
                    bloco.config(bg="blue", fg="black")

                if self.blocos[j][i].estado == "fim":
                    bloco.config(bg="red", fg="black")

                if self.blocos[j][i].estado == "caminho":
                    bloco.config(bg="green", fg="black")

                if self.blocos[j][i].estado == "marcado":
                    bloco.config(bg="gray", fg="red")

                if self.blocos[j][i].estado == "parede":
                    bloco.config(bg="black", fg="white")

                bloco.grid(row=j, column=i)
                campo[j][i] = bloco

    def waveFront(self):
        wave_number = 0

        while (
            self.blocos[self.inicio.j][self.inicio.i].valor == 0
            and wave_number < max([self.linhas, self.colunas]) + 1
        ):
            for j in range(self.colunas):
                for i in range(self.linhas):
                    if (
                        self.blocos[j][i].estado == "marcado"
                        or self.blocos[j][i].estado == "fim"
                    ) and self.blocos[j][i].valor == wave_number:
                        vizinhos = [(j - 1, i), (j + 1, i), (j, i - 1), (j, i + 1)]

                        for jAux, iAux in vizinhos:
                            if (
                                0 <= jAux < self.colunas
                                and 0 <= iAux < self.linhas
                                and (
                                    self.blocos[jAux][iAux].estado == "vazio"
                                    or self.blocos[jAux][iAux].estado == "inicio"
                                )
                            ):
                                self.blocos[jAux][iAux].valor = wave_number + 1
                                if self.blocos[jAux][iAux].estado == "vazio":
                                    self.blocos[jAux][iAux].estado = "marcado"

            wave_number += 1

    def gerarCaminho(self):
        blocoAtual = copy.copy(self.inicio)
        passos = 0

        while not (blocoAtual.i == self.fim.i and blocoAtual.j == self.fim.j):
            vizinhos = [
                (blocoAtual.j - 1, blocoAtual.i),
                (blocoAtual.j + 1, blocoAtual.i),
                (blocoAtual.j, blocoAtual.i - 1),
                (blocoAtual.j, blocoAtual.i + 1),
            ]

            opcao = []

            for jAux, iAux in vizinhos:
                if (
                    0 <= jAux < self.colunas
                    and 0 <= iAux < self.linhas
                    and self.blocos[jAux][iAux].estado == "marcado"
                    and self.blocos[jAux][iAux].valor < blocoAtual.valor
                ):
                    opcao.append(self.blocos[jAux][iAux])

            if len(opcao) != 0:
                escolha = random.choice(opcao)
            else:
                return

            self.blocos[escolha.j][escolha.i].estado = "caminho"
            blocoAtual = copy.copy(escolha)

            passos += 1


root = tk.Tk()
root.title("Path Finder")
root.state("zoomed")
frame = Frame(root)
frame.grid()


campo = Campo(frame, 20, 20)

campo.gerarInicio()
campo.gerarFim()
# campo.gerarObstaculos()
campo.waveFront()
campo.gerarCaminho()
campo.criarInterface()

root.mainloop()
