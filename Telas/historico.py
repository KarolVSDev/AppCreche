import tkinter as tk
from tkinter import ttk

class TelaHistorico:
    def __init__(self, root):
        self.root = root
        self.root.title("Histórico de Saídas")

        self.lista_registros = ttk.Treeview(root, columns=("Data", "Hora"), show="headings")
        self.lista_registros.heading("Data", text="Data")
        self.lista_registros.heading("Hora", text="Hora")
        self.lista_registros.pack(padx=20, pady=20)

        self.botao_filtrar = tk.Button(root, text="Filtrar", command=self.filtrar_registros)
        self.botao_filtrar.pack(pady=10)

        self.botao_buscar = tk.Button(root, text="Buscar", command=self.buscar_registro)
        self.botao_buscar.pack(pady=10)

        # Simulação de dados iniciais
        self.registros = [
            {"data": "2024-06-25", "hora": "09:30"},
            {"data": "2024-06-24", "hora": "15:00"},
            {"data": "2024-06-23", "hora": "12:45"},
            # Adicione mais registros conforme necessário
        ]

        self.atualizar_lista_registros()

    def atualizar_lista_registros(self):
        # Limpa os registros antigos da lista
        for registro in self.lista_registros.get_children():
            self.lista_registros.delete(registro)

        # Insere os novos registros na lista
        for registro in self.registros:
            self.lista_registros.insert("", "end", values=(registro["data"], registro["hora"]))

    def filtrar_registros(self):
        # Aqui você pode implementar a lógica para filtrar os registros (ainda não implementado)
        messagebox.showinfo("Filtrar", "Funcionalidade de filtrar será implementada posteriormente.")

    def buscar_registro(self):
        # Aqui você pode implementar a lógica para buscar registros (ainda não implementado)
        messagebox.showinfo("Buscar", "Funcionalidade de buscar será implementada posteriormente.")

# Exemplo de chamada da tela de histórico
root = tk.Tk()
tela_historico = TelaHistorico(root)
root.mainloop()
