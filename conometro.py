import tkinter as tk
from tkinter import ttk
import threading
import time

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.tempo_atual = tk.StringVar()
        self.tempo_atual.set("00:00:00")

        self.label_tempo = ttk.Label(root, textvariable=self.tempo_atual, font=("Arial", 24))
        self.label_tempo.pack(pady=10)

        self.botao_iniciar = ttk.Button(root, text="Iniciar", command=self.iniciar_cronometro)
        self.botao_iniciar.pack(side=tk.LEFT, padx=5)

        self.botao_parar = ttk.Button(root, text="Parar", command=self.parar_cronometro)
        self.botao_parar.pack(side=tk.LEFT, padx=5)

        self.botao_resetar = ttk.Button(root, text="Resetar", command=self.resetar_cronometro)
        self.botao_resetar.pack(side=tk.LEFT, padx=5)

        self.tempo_inicio = None
        self.tempo_decorrido = 0
        self.running = False

    def iniciar_cronometro(self):
        if not self.running:
            self.tempo_inicio = time.time() - self.tempo_decorrido
            self.running = True
            self.atualizar_tempo()

    def parar_cronometro(self):
        if self.running:
            self.running = False

    def resetar_cronometro(self):
        self.parar_cronometro()
        self.tempo_decorrido = 0
        self.tempo_atual.set("00:00:00")

    def atualizar_tempo(self):
        if self.running:
            self.tempo_decorrido = time.time() - self.tempo_inicio
            horas = int(self.tempo_decorrido // 3600)
            minutos = int((self.tempo_decorrido % 3600) // 60)
            segundos = int(self.tempo_decorrido % 60)
            tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.tempo_atual.set(tempo_formatado)
            self.root.after(1000, self.atualizar_tempo)  # Atualiza a cada segundo

if __name__ == "__main__":
    root = tk.Tk()
    app = Cronometro(root)
    root.mainloop()