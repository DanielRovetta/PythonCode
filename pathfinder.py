import tkinter as tk
from tkinter import *
import random
import copy
import math


class Bloco:
    i: int
    j: int
    estado: str
    valor: int
    dh: str
    dv: str

    def __init__(self, i, j, valor, estado):
        self.i = i
        self.j = j
        self.valor = valor
        self.estado = estado

        if self.j == 0 or self.j % 2 == 0:
            self.dh = "b"
        else:
            self.dh = "c"

        if self.i == 0 or self.i % 2 == 0:
            self.dv = "e"
        else:
            self.dv = "d"


class Campo:
    def __init__(self, root, linhas, colunas):
        self.root = root
        self.linhas = linhas
        self.colunas = colunas

        self.criarCampo()

    def criarCampo(self):
        self.blocos = [[None] * self.colunas for _ in range(self.linhas)]

        for i in range(self.linhas):
            for j in range(self.colunas):
                bloco = Bloco(i, j, 0, "vazio")
                self.blocos[i][j] = bloco

    def gerarObstaculos(self):
        i = random.randint(0, self.linhas - 1)
        j = random.randint(0, self.colunas - 1)

        while self.blocos[i][j].estado != "vazio":
            i = random.randint(0, self.linhas - 1)
            j = random.randint(0, self.colunas - 1)

        self.blocos[i][j].valor = 0
        self.blocos[i][j].estado = "parede"

    def gerarInicio(self):
        i = random.randint(0, self.linhas - 1)
        j = random.randint(0, self.colunas - 1)

        while self.blocos[i][j].estado != "vazio":
            i = random.randint(0, self.linhas - 1)
            j = random.randint(0, self.colunas - 1)

        self.blocos[i][j].valor = 0
        self.blocos[i][j].estado = "inicio"
        self.blocos[i][j].i = i
        self.blocos[i][j].j = j

        self.inicio = self.blocos[i][j]

    def gerarFim(self):
        i = random.randint(0, self.linhas - 1)
        j = random.randint(0, self.colunas - 1)

        while self.blocos[i][j].estado != "vazio":
            i = random.randint(0, self.linhas - 1)
            j = random.randint(0, self.colunas - 1)

        self.blocos[i][j].valor = 0
        self.blocos[i][j].estado = "fim"
        self.blocos[i][j].i = i
        self.blocos[i][j].j = j

        self.fim = self.blocos[i][j]

    def criarInterface(self):
        campo = [[None] * self.colunas for _ in range(self.linhas)]
        for i in range(self.linhas):
            for j in range(self.colunas):
                bloco = tk.Label(
                    self.root,
                    width=7,
                    height=3,
                    text=str(self.blocos[i][j].valor)
                    + "\n"
                    + self.blocos[i][j].dh
                    + ":"
                    + self.blocos[i][j].dv
                    + "\n"
                    + str(self.blocos[i][j].i)
                    + ":"
                    + str(self.blocos[i][j].j),
                    bd=0.5,
                    relief="solid",
                    bg="white",
                )
                if self.blocos[i][j].estado == "vazio":
                    bloco.config(
                        bg="white",
                        fg="black",
                    )

                if self.blocos[i][j].estado == "inicio":
                    bloco.config(bg="blue", fg="black")

                if self.blocos[i][j].estado == "fim":
                    bloco.config(bg="red", fg="black")

                if self.blocos[i][j].estado == "caminho":
                    bloco.config(bg="green", fg="black")

                if self.blocos[i][j].estado == "marcado":
                    bloco.config(bg="gray", fg="red")

                if self.blocos[i][j].estado == "parede":
                    bloco.config(bg="black", fg="white")

                bloco.grid(row=i, column=j)
                campo[i][j] = bloco

    def waveFront(self):
        wave_number = 0

        while (
            self.blocos[self.inicio.i][self.inicio.j].valor == 0
            and wave_number < self.linhas * self.colunas
        ):
            for i in range(self.colunas):
                for j in range(self.linhas):
                    if (
                        self.blocos[i][j].estado == "marcado"
                        or self.blocos[i][j].estado == "fim"
                    ) and self.blocos[i][j].valor == wave_number:
                        vizinhos = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

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

        while not (blocoAtual.j == self.fim.j and blocoAtual.i == self.fim.i):
            print(
                "Atual: I:",
                blocoAtual.i,
                "J:",
                blocoAtual.j,
                "Direcao:",
                blocoAtual.dh + ":" + blocoAtual.dv,
                "Valor:",
                blocoAtual.valor,
                "Estado:",
                blocoAtual.estado,
            )

            print()
            vizinhos = []

            if blocoAtual.dh == "c":
                vizinhos.append((blocoAtual.i - 1, blocoAtual.j))

            if blocoAtual.dh == "b":
                vizinhos.append((blocoAtual.i + 1, blocoAtual.j))

            if blocoAtual.dv == "e":
                vizinhos.append((blocoAtual.i, blocoAtual.j - 1))

            if blocoAtual.dv == "d":
                vizinhos.append((blocoAtual.i, blocoAtual.j + 1))

            for i, j in vizinhos:
                print(
                    "Vizinhos: I:",
                    i,
                    "J:",
                    j,
                )
            print()

            opcao = []

            for jAux, iAux in vizinhos:
                if (
                    0 <= jAux < self.colunas
                    and 0 <= iAux < self.linhas
                    and (
                        self.blocos[jAux][iAux].estado == "marcado"
                        or self.blocos[jAux][iAux].estado == "vazio"
                        or self.blocos[jAux][iAux].estado == "fim"
                    )
                    and (
                        self.blocos[jAux][iAux].valor < blocoAtual.valor
                        or self.blocos[jAux][iAux].valor == 0
                        or blocoAtual.valor == 0
                    )
                ):
                    print(
                        "Bloco: I:",
                        self.blocos[jAux][iAux].i,
                        "J:",
                        self.blocos[jAux][iAux].j,
                        "Direcao:",
                        self.blocos[jAux][iAux].dh + ":" + self.blocos[jAux][iAux].dv,
                        "Valor:",
                        self.blocos[jAux][iAux].valor,
                        "Estado:",
                        self.blocos[jAux][iAux].estado,
                    )
                    opcao.append(self.blocos[jAux][iAux])

            for o in opcao:
                print(
                    "Opcao: I:",
                    o.i,
                    "J:",
                    o.j,
                    "Valor:",
                    o.valor,
                    "Estado:",
                    o.estado,
                    "Distacia:",
                    math.sqrt((self.fim.i - o.i) ** 2 + (self.fim.j - o.j) ** 2),
                )
            print()

            if len(opcao) != 0:
                escolha = min(
                    opcao,
                    key=lambda obj: math.sqrt(
                        (self.fim.i - obj.i) ** 2 + (self.fim.j - obj.j) ** 2
                    ),
                )
                print(
                    "Escolha: I:",
                    escolha.i,
                    "J:",
                    escolha.j,
                    "Valor:",
                    escolha.valor,
                    "Estado:",
                    escolha.estado,
                )
                print()

            else:
                for jAux, iAux in vizinhos:
                    if (
                        0 <= jAux < self.colunas
                        and 0 <= iAux < self.linhas
                        and (
                            self.blocos[jAux][iAux].estado == "marcado"
                            or self.blocos[jAux][iAux].estado == "vazio"
                        )
                    ):
                        print(
                            "Bloco: I:",
                            self.blocos[jAux][iAux].i,
                            "J:",
                            self.blocos[jAux][iAux].j,
                            "Direcao:",
                            self.blocos[jAux][iAux].dh
                            + ":"
                            + self.blocos[jAux][iAux].dv,
                            "Valor:",
                            self.blocos[jAux][iAux].valor,
                            "Estado:",
                            self.blocos[jAux][iAux].estado,
                        )
                        opcao.append(self.blocos[jAux][iAux])

                for o in opcao:
                    print(
                        "Opcao: I:",
                        o.i,
                        "J:",
                        o.j,
                        "Valor:",
                        o.valor,
                        "Estado:",
                        o.estado,
                        "Distacia:",
                        math.sqrt((self.fim.i - o.i) ** 2 + (self.fim.j - o.j) ** 2),
                    )
                print()

                if len(opcao) != 0:
                    escolha = min(
                        opcao,
                        key=lambda obj: math.sqrt(
                            (self.fim.i - obj.i) ** 2 + (self.fim.j - obj.j) ** 2
                        ),
                    )
                    print(
                        "Escolha: I:",
                        escolha.i,
                        "J:",
                        escolha.j,
                        "Valor:",
                        escolha.valor,
                        "Estado:",
                        escolha.estado,
                    )
                    print()
                else:
                    return

            if self.blocos[escolha.i][escolha.j].estado != "fim":
                self.blocos[escolha.i][escolha.j].estado = "caminho"
            blocoAtual = copy.copy(escolha)

            passos += 1


root = tk.Tk()
root.title("Path Finder")
# root.state("zoomed")
frame = Frame(root)
frame.grid()


campo = Campo(frame, 10, 10)

campo.gerarInicio()
campo.gerarFim()
# campo.gerarObstaculos()
campo.waveFront()
campo.criarInterface()
campo.gerarCaminho()
campo.criarInterface()

root.mainloop()
