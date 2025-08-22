# Atividade 4 - Sistema de senhas

import tkinter as tk
from tkinter import messagebox

# Configurando janela principal
janela = tk.Tk()
janela.title("Validação de senha!")
janela.geometry("300x300")

# Função de verificação de senhas
def verificar_senha():
    senha_entry = (entry_senha.get())
    senha = "1234"
    if senha_entry == senha:
        messagebox.showinfo("Boas-vindas!", "Acesso permitido!")
    elif senha_entry != senha:
        messagebox.showinfo("Erro!", "Senha incorreta. Acesso negado!")
    texto_senha.set("")
    

# Título do corpo da página
titulo_janela = tk.Label(janela, text="Verificação de acesso", font=("Arial", 14))
titulo_janela.pack(pady=15)

rotulo1 = tk.Label(janela, text="Digite sua senha", font=("Arial", 12))
rotulo1.pack(pady=10)

# Entrada
texto_senha = tk.StringVar()
entry_senha = tk.Entry(janela, textvariable=texto_senha, width=15, show="*")
entry_senha.pack(pady=5)

btn_enviar = tk.Button(janela, text="Enviar", command=verificar_senha)
btn_enviar.pack(pady=5)


janela.mainloop()
