# Atividade 5 - Cardápio interativo

import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title("Cardápioo")
# janela.geometry("300x400")


def enviar_pedido():
    pedido_entry = codigo_entry.get()
    qtd = int(qtd_entry.get())
    total = float(rotulo_total2["text"])
    try:
        if pedido_entry == "1":
            pedido = f"{qtd} Pizza – R$ 30,00\n"
            total += (30*qtd)
        elif pedido_entry == "2":
            pedido = f"{qtd} Hambúrguer – R$ 20,00\n"
            total += (20*qtd)
        elif pedido_entry == "3":
            pedido = f"{qtd} Refrigerante – R$ 5,00\n"
            total += (5*qtd)
        else:
            raise ValueError("Opção inválida!")
    except ValueError as e:
        texto_cod_entry.set("")
        messagebox.showinfo("Erro", f"{e}!")
        return


    rotulo_itens["text"] += pedido
    texto_cod_entry.set("") # Limpando caixa de input
    rotulo_total2["text"] = f"{total:.2f}"
    
   
# Cardápio com opções
titulo_corpo = tk.Label(janela, text="Faça seu pedido!", font=("Helvetica", 14))
titulo_corpo.pack(pady=10, padx=100)

rotulo1 = tk.Label(janela, text="1 - Pizza – R$ 30,00")
rotulo1.pack(pady=1)

rotulo2 = tk.Label(janela, text="2 - Hambúrguer – R$ 20,00")
rotulo2.pack(pady=1)

rotulo3 = tk.Label(janela, text="3 - Refrigerante – R$ 5,00")
rotulo3.pack(pady=1)

# Espaço de exibição do pedido
rotulo_itens_pedidos = tk.Label(janela, text="PEDIDO: ", font=("Helvetica", 10))
rotulo_itens_pedidos.pack(pady=20)

# pedido_texto = tk.StringVar()
rotulo_itens = tk.Label(janela, text="", font=("Helvetica", 10))
rotulo_itens.pack()

# Declarando widgets da parte inferior
rotulo_codigo = tk.Label(janela, text="Código: ")
rotulo_qtd = tk.Label(janela, text="Quantidade: ")

# Input código do pedido
texto_cod_entry = tk.StringVar() # Para limpar caixa de input posteriormente
codigo_entry = tk.Entry(janela, textvariable=texto_cod_entry, width=5)

# Input código do pedido
texto_qtd_entry = tk.StringVar() # Para limpar caixa de input posteriormente
qtd_entry = tk.Entry(janela, textvariable=texto_qtd_entry, width=5)
btn_enviar = tk.Button(janela, text="Enviar pedido", command=enviar_pedido)

rotulo_total = tk.Label(janela, text="Total = R$", font=("Helvetica", 12))
rotulo_total2 = tk.Label(janela, text="0.00", font=("Helvetica", 12), fg="red")

# Organizando widgets da parte inferior
rotulo_total2.pack(side="bottom")
rotulo_total.pack(pady=2, side="bottom")
btn_enviar.pack(pady=10, side="bottom")

qtd_entry.pack(pady=5, side="bottom")
rotulo_qtd.pack(side="bottom")
codigo_entry.pack(pady=5, side="bottom")
rotulo_codigo.pack(side="bottom")


janela.mainloop()
