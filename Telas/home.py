import tkinter as tk
from tkinter import messagebox


def escanear_qr_code():
    # Aqui você pode adicionar a lógica para escanear o QR Code
    messagebox.showinfo("QR Code", "Aqui você faria a leitura do QR Code.")


# Função para abrir a tela Home
def abrir_tela_home():
    # Criar a janela principal da tela Home
    root = tk.Tk()
    root.title("Tela Home")

    # Criar um botão para escanear o QR Code
    botao_scan_qr = tk.Button(root, text="Escanear QR Code", command=escanear_qr_code)
    botao_scan_qr.pack(pady=20)

    # Outras funcionalidades do sistema podem ser adicionadas aqui

    # Iniciar o loop principal da aplicação
    root.mainloop()


# Exemplo de chamada da função para abrir a tela Home
abrir_tela_home()
