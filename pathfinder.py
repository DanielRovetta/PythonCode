import tkinter as tk
import random


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
        # print(self.inicio.i)
        # print(self.inicio.j)
        # print()
        # print(self.fim.i)
        # print(self.fim.j)

        # print()
        # print(self.blocos[self.inicio.j][self.inicio.i].estado)
        # print(self.blocos[self.inicio.j][self.inicio.i].valor)
        # print()
        # print(self.blocos[self.fim.j][self.fim.i].estado)
        # print(self.blocos[self.fim.j][self.fim.i].valor)

        wave_number = 0

        while self.blocos[self.fim.j][self.fim.i].valor == 0:
            print(wave_number)

            for j in range(self.colunas):
                for i in range(self.linhas):
                    if (
                        self.blocos[j][i].estado == "marcado"
                        or self.blocos[j][i].estado == "fim"
                    ) and self.blocos[j][i].valor == wave_number:
                        print(self.blocos[j][i].estado)
                        print(self.blocos[j][i].valor)
                        print(j, i)

                    if (
                        self.blocos[j][i].estado == "marcado"
                        or self.blocos[j][i].estado == "fim"
                    ) and self.blocos[j][i].valor == wave_number:
                        vizinhos = [
                            (j - 1, i),
                            (j + 1, i),
                            (j, i - 1),
                            (j, i + 1),
                            (j - 1, i - 1),
                            (j - 1, i + 1),
                            (j + 1, i - 1),
                            (j + 1, i + 1),
                        ]

                        for jAux, iAux in vizinhos:
                            print(
                                0 <= jAux < self.colunas
                                and 0 <= iAux < self.linhas
                                and self.blocos[jAux][iAux].estado == "vazio"
                            )
                            print()

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


root = tk.Tk()
root.title("Malha Quadriculada")
campo = Campo(root, 20, 20)

campo.gerarInicio()
campo.gerarFim()
campo.gerarObstaculos()
campo.gerarObstaculos()
campo.gerarObstaculos()
campo.gerarObstaculos()
campo.gerarObstaculos()
campo.waveFront()
campo.criarInterface()

root.mainloop()
