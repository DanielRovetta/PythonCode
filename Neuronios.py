import numpy as np


class Aprendizado:
    dados: any
    pesos: any
    resultados: any
    saida: any
    ciclos: int

    def __init__(self, dados, resultados, ciclos):
        self.dados = dados
        self.resultados = resultados
        self.ciclos = ciclos

    def aprender(self):
        # np.random.seed(1)
        self.pesos = 2 * np.random.random((len(self.dados[0]), 1)) - 1

        for i in range(self.ciclos):
            dadosAux = self.dados
            self.saida = self.sigmoid(np.dot(dadosAux, self.pesos))
            erro = self.resultados - self.saida
            ajuste = erro * self.sigmoid_derivative(self.saida)
            self.pesos += np.dot(dadosAux.T, ajuste)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)


class Processamento:
    pesos: any
    entrada: any
    saida: any

    def __init__(self, pesos, entrada):
        self.pesos = pesos
        self.entrada = entrada

    def processar(self):
        self.saida = 1 / (1 + np.exp(-np.dot(self.entrada, self.pesos)))
