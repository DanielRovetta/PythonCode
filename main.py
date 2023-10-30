from Neuronios import Aprendizado, Processamento
import numpy as np

dados = np.array(
    [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1],
    ]
)

resultado = np.array([[0, 0, 0, 0, 1, 1, 1, 1]]).T

aprendizado = Aprendizado(dados, resultado, 100000)
aprendizado.aprender()

entradas = np.array([[0, 0, 0], [1, 1, 1], [1, 0, 0]])
processamento = Processamento(aprendizado.pesos, entradas)
processamento.processar()

print(processamento.saida)
