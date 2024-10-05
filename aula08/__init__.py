import tkinter as tk

def botao_clicado():
    print(f"Botão clicado! digtou: {entrada.get()}")

janela = tk.Tk()
janela.title("Minha primeira janela com Tkinter")

rotulo = tk.Label(janela, text = "Olá, mundo!")
rotulo.pack()

botao = tk.Button(janela, text="Clique aqui", command=botao_clicado)
botao.pack()

entrada = tk.Entry(janela)
entrada.pack()

janela.mainloop()