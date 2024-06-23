import tkinter as tk
from tkinter import messagebox

class TelaConfirmacao:
    def __init__(self, root, dados_crianca):
        self.root = root
        self.root.title("Tela de Confirmação")

        self.label_info = tk.Label(root, text=f"Informações da Criança:\n{dados_crianca}")
        self.label_info.pack(pady=20)

        self.botao_confirmar = tk.Button(root, text="Confirmar Saída", command=self.confirmar_saida)
        self.botao_confirmar.pack(side=tk.LEFT, padx=20)

        self.botao_cancelar = tk.Button(root, text="Cancelar", command=self.cancelar_saida)
        self.botao_cancelar.pack(side=tk.RIGHT, padx=20)

    def confirmar_saida(self):
        messagebox.showinfo("Confirmação", "Saída confirmada!")
        self.root.destroy()  # Fecha a janela de confirmação

    def cancelar_saida(self):
        messagebox.showinfo("Cancelamento", "Operação cancelada.")
        self.root.destroy()  # Fecha a janela de confirmação

# Exemplo de chamada da tela de confirmação
def abrir_tela_confirmacao(dados_crianca):
    root = tk.Tk()
    tela_confirmacao = TelaConfirmacao(root, dados_crianca)
    root.mainloop()

# Simulando dados da criança associada ao QR Code
dados_crianca = {
    "Nome": "Ana Silva",
    "Idade": "5 anos",
    "Responsável": "João Silva",
    "Localização": "Sala 1",
    # Adicione mais informações conforme necessário
}

# Chamada da tela de confirmação com os dados simulados
abrir_tela_confirmacao(dados_crianca)
