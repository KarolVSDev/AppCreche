import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import pyzbar.pyzbar as pyzbar

class LeitorQRCode:
    def __init__(self, root):
        self.root = root
        self.root.title("Leitura de QR Code")

        self.camera = cv2.VideoCapture(0)  # Inicializa a captura de vídeo da câmera
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.botao_iniciar = tk.Button(root, text="Iniciar Leitura", command=self.iniciar_leitura)
        self.botao_iniciar.pack(pady=20)

        self.botao_parar = tk.Button(root, text="Parar Leitura", command=self.parar_leitura)
        self.botao_parar.pack(pady=10)
        self.botao_parar.config(state=tk.DISABLED)

        self.frame_atual = None
        self.lendo_qr = False

    def iniciar_leitura(self):
        self.lendo_qr = True
        self.botao_iniciar.config(state=tk.DISABLED)
        self.botao_parar.config(state=tk.NORMAL)
        self.leitura_qr()

    def parar_leitura(self):
        self.lendo_qr = False
        self.botao_iniciar.config(state=tk.NORMAL)
        self.botao_parar.config(state=tk.DISABLED)

    def leitura_qr(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.frame_atual = Image.fromarray(frame)
            img = ImageTk.PhotoImage(self.frame_atual)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

            # Realiza a leitura de QR Code
            decoded_objs = pyzbar.decode(frame)

            for obj in decoded_objs:
                print("Dados do QR Code:", obj.data)
                messagebox.showinfo("QR Code", f"Dados do QR Code: {obj.data.decode('utf-8')}")

        if self.lendo_qr:
            self.root.after(10, self.leitura_qr)  # Chama recursivamente a função a cada 10 milissegundos

# Criar a janela principal
root = tk.Tk()
leitor = LeitorQRCode(root)

# Iniciar o loop principal da aplicação
root.mainloop()
