import tkinter as tk
from tkinter import messagebox


def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Aqui você pode adicionar a lógica de validação do login
    # Por exemplo, verificar se o usuário e senha estão corretos

    if usuario == "usuario123" and senha == "senha123":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        # Aqui você pode adicionar o código para abrir a próxima tela após o login
    else:
        messagebox.showerror("Login", "Nome/Matrícula de usuário ou senha incorretos!")


# Criar a janela principal
root = tk.Tk()
root.title("Tela de Login")

# Criar os widgets da tela de login
label_usuario = tk.Label(root, text="Nome/Matrícula do Usuário:")
label_usuario.pack()

entry_usuario = tk.Entry(root)
entry_usuario.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack()

entry_senha = tk.Entry(root, show="*")  # A senha será mostrada como asteriscos
entry_senha.pack()

botao_login = tk.Button(root, text="Login", command=fazer_login)
botao_login.pack()

# Iniciar o loop principal da aplicação
root.mainloop()
