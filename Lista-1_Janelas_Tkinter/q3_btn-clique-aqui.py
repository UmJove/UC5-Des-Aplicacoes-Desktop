# 3. Você quer adicionar um botão chamado "Clique aqui" na tela principal do programa.
# Escreva o código necessário para criar e exibir esse botão na janela.

import tkinter as tk

def abrir_janela2():
    janela2 = tk.Tk()
    janela2.title("Janela 2")
    janela2.geometry("200x200")

    rotulo = tk.Label(janela2, text="Você clicou!")
    rotulo.pack(pady=50)

root = tk.Tk()
root.title("Janela Principal")
root.geometry("200x200")

btn_fechar = tk.Button(root, text="Clique aqui!", command=abrir_janela2)
btn_fechar.pack(pady=50)

root.mainloop()