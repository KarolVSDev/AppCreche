import tkinter as tk
from tkinter import ttk

class TelaConfiguracoes:
    def __init__(self, root):
        self.root = root
        self.root.title("Configurações do Aplicativo")

        # Frame para opções de idioma
        frame_idioma = ttk.LabelFrame(root, text="Idioma")
        frame_idioma.pack(padx=20, pady=20, fill=tk.BOTH)

        self.opcao_idioma = tk.StringVar()
        self.opcao_idioma.set("Português")  # Idioma padrão
        idiomas = ["Português", "Inglês", "Espanhol"]  # Opções de idioma

        for idioma in idiomas:
            rb = ttk.Radiobutton(frame_idioma, text=idioma, variable=self.opcao_idioma, value=idioma)
            rb.pack(anchor=tk.W)

        # Frame para opções de notificações
        frame_notificacoes = ttk.LabelFrame(root, text="Notificações")
        frame_notificacoes.pack(padx=20, pady=20, fill=tk.BOTH)

        self.notif_ativadas = tk.BooleanVar()
        self.notif_ativadas.set(True)  # Notificações ativadas por padrão

        check_notif = ttk.Checkbutton(frame_notificacoes, text="Ativar notificações", variable=self.notif_ativadas)
        check_notif.pack(anchor=tk.W)

        # Botão para salvar as configurações
        botao_salvar = ttk.Button(root, text="Salvar Configurações", command=self.salvar_configuracoes)
        botao_salvar.pack(pady=10)

    def salvar_configuracoes(self):
        idioma_selecionado = self.opcao_idioma.get()
        notif_ativadas = self.notif_ativadas.get()

        # Aqui você pode implementar a lógica para salvar as configurações
        mensagem = f"Configurações salvas:\nIdioma: {idioma_selecionado}\nNotificações: {'Ativadas' if notif_ativadas else 'Desativadas'}"
        tk.messagebox.showinfo("Configurações Salvas", mensagem)

# Exemplo de chamada da tela de configurações
root = tk.Tk()
tela_configuracoes = TelaConfiguracoes(root)
root.mainloop()
