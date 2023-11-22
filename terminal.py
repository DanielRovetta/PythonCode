import tkinter as tk
from tkinter import scrolledtext


class TerminalSimulado:
    def __init__(self, master):
        self.master = master
        master.title("Terminal Simulado")

        self.entrada = tk.Entry(master, width=50)
        self.entrada.pack(pady=10)

        self.botao_executar = tk.Button(
            master, text="Executar", command=self.executar_comando
        )
        self.botao_executar.pack()

        self.area_texto = scrolledtext.ScrolledText(
            master, wrap=tk.WORD, width=60, height=15
        )
        self.area_texto.pack()

    def executar_comando(self):
        # Obter o comando da entrada
        comando = self.entrada.get()

        # Simular a execução do comando
        resultado = f"Comando executado: {comando}\n"

        # Adicionar o resultado à área de texto
        self.area_texto.insert(tk.END, resultado)

        # Limpar a entrada
        self.entrada.delete(0, tk.END)


# Criar a janela principal
root = tk.Tk()

# Criar uma instância do terminal simulado
terminal = TerminalSimulado(root)

# Iniciar o loop principal
root.mainloop()
