# 8. Imagine que você está desenvolvendo um programa de aviso.
# Crie uma janela com um rótulo (Label) escrito "Atenção!" em fonte grande e em vermelho.
import tkinter as tk

janela = tk.Tk()
janela.title("Atenção!")
janela.geometry("300x200")

rotulo_atencao = tk.Label(janela, text="ATENÇÃO!!!", font=("Arial", 22), foreground="red")
rotulo_atencao.pack(pady=50)

janela.mainloop()