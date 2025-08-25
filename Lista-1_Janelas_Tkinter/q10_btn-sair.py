# 10. Você quer fazer um botão que, ao ser clicado, fecha a janela principal.
# Crie o programa em Tkinter com um botão chamado "Sair", que encerra a aplicação.

import tkinter as tk

janela = tk.Tk()
janela.title("Principal")
janela.geometry("200x200")

btn_sair = tk.Button(janela, text="sair", command=janela.destroy)
btn_sair.pack(pady=50)

janela.mainloop()