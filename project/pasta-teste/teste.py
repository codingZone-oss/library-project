import tkinter as tk
from tkinter import ttk, messagebox

class SistemaBancario:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema Bancário")
        self.root.geometry("800x600")
        self.root.state("zoomed")  # Tela cheia

        # Configurar grid principal
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Frame principal
        self.main_frame = tk.Frame(self.root, bg="salmon")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Título
        titulo = tk.Label(self.main_frame, text="Sistema de Funcionários", font=("Arial", 16), bg="lightgray")
        titulo.pack(pady=20)

        # Formulário
        self.criar_formulario()

        # Botão
        botao = tk.Button(self.main_frame, text="Salvar", command=self.salvar, bg="green", fg="white")
        botao.pack(pady=10)

    def criar_formulario(self):
        # Frame do formulário
        form_frame = tk.Frame(self.main_frame, bg="white", relief="groove", bd=2)
        form_frame.pack(pady=20, padx=50, fill="x")

        # Campos
        tk.Label(form_frame, text="Nome:", bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entrada_nome = tk.Entry(form_frame, font=("Arial", 12))
        self.entrada_nome.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="CPF:", bg="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.entrada_cpf = tk.Entry(form_frame, font=("Arial", 12))
        self.entrada_cpf.grid(row=1, column=1, padx=10, pady=5)

    def salvar(self):
        nome = self.entrada_nome.get()
        cpf = self.entrada_cpf.get()
        if not nome or not cpf:
            messagebox.showwarning("Erro", "Preencha todos os campos!")
        else:
            messagebox.showinfo("Sucesso", f"Funcionário {nome} salvo com CPF {cpf}")

    def run(self):
        self.root.mainloop()

app = SistemaBancario()
app.run()