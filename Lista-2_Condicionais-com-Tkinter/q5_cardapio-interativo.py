# Atividade 5 - Cardápio interativo

import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title("Cardápio")
janela.geometry("300x400")


def enviar_pedido():
    pedido_entry = codigo_entry.get()

    if pedido_entry == "1":
        pedido = "Pizza – R$ 30,00"
    elif pedido_entry == "2":
        pedido = "Hambúrguer – R$ 20,00"
    elif pedido_entry == "3":
        pedido = "Refrigerante – R$ 5,00"
    else:
        messagebox.showinfo("Erro", "Opção inválida!")
    
    pedido_texto.set(f"{pedido}")
    texto_entry.set("") # Limpando caixa de input
    
    
   
# Cardápio com opções
titulo_corpo = tk.Label(janela, text="Faça seu pedido!", font=("Helvetica", 14))
titulo_corpo.pack(pady=10)

rotulo1 = tk.Label(janela, text="1 - Pizza – R$ 30,00")
rotulo1.pack(pady=1)

rotulo2 = tk.Label(janela, text="2 - Hambúrguer – R$ 20,00")
rotulo2.pack(pady=1)

rotulo3 = tk.Label(janela, text="3 - Refrigerante – R$ 5,00")
rotulo3.pack(pady=1)

# Espaço de exibição do pedido
rotulo_itens_pedidos = tk.Label(janela, text="PEDIDO: ", font=("Helvetica", 12))
rotulo_itens_pedidos.pack(pady=20)

pedido_texto = tk.StringVar()
rotulo_itens = tk.Label(janela, textvariable=pedido_texto, font=("Helvetica", 12))
rotulo_itens.pack()

# Declarando widgets da parte inferior
rotulo_entry = tk.Label(janela, text="Código: ")
texto_entry = tk.StringVar() # Para limpar caixa de input
codigo_entry = tk.Entry(janela, textvariable=texto_entry, width=5)
btn_enviar = tk.Button(janela, text="Enviar pedido", command=enviar_pedido)


# Organizando widgets da parte inferior
btn_enviar.pack(pady=10, side="bottom")
codigo_entry.pack(pady=5, side="bottom")
rotulo_entry.pack(side="bottom")



janela.mainloop()
