# 5. Em uma aplicação, ao clicar em um botão, você quer abrir uma nova janela chamada "Segunda Tela".
# Escreva o código em Tkinter que cria essa nova janela a partir da tela principal.

import tkinter as tk

cont = 0

def abrir_nova_janela():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Nova Janela")
    nova_janela.geometry("300x300")

    rotulo_nj1 = tk.Label(nova_janela, text="Esta é a nova janela que você pediu!")
    rotulo_nj1.pack(pady=50)
  


root = tk.Tk()
root.title("Janela Principal")
root.geometry("300x300")

rotulo1 = tk.Label(root, text="Rótulo Hum")
rotulo1.pack(pady=50)

btn_nova_janela = tk.Button(root, text="Abri nova janela!", command=abrir_nova_janela)
btn_nova_janela.pack(pady=50)


root.mainloop() 