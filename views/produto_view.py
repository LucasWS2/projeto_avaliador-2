import tkinter as tk
from tkinter import messagebox, ttk
from controllers.produto_controller import ProdutoController

class ProdutoView:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Cadastro de Produtos")
        self.root.geometry("400x400")

        tk.Label(self.root, text="Nome do Produto:").pack()
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack()

        tk.Label(self.root, text="Preço (R$):").pack()
        self.preco_entry = tk.Entry(self.root)
        self.preco_entry.pack()

        tk.Label(self.root, text="Estoque:").pack()
        self.estoque_entry = tk.Entry(self.root)
        self.estoque_entry.pack()

        tk.Button(self.root, text="Cadastrar", command=self.cadastrar_produto).pack(pady=10)

        self.tabela = ttk.Treeview(self.root, columns=("ID", "Nome", "Preço", "Estoque"), show="headings")
        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Preço", text="Preço")
        self.tabela.heading("Estoque", text="Estoque")
        self.tabela.pack(pady=10, fill=tk.BOTH, expand=True)

        self.atualizar_tabela()

    def cadastrar_produto(self):
        nome = self.nome_entry.get()
        preco = self.preco_entry.get()
        estoque = self.estoque_entry.get()

        try:
            preco_float = float(preco)
            estoque_int = int(estoque)
            ProdutoController.cadastrar(nome, preco_float, estoque_int)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            self.nome_entry.delete(0, tk.END)
            self.preco_entry.delete(0, tk.END)
            self.estoque_entry.delete(0, tk.END)
            self.atualizar_tabela()
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser número decimal e estoque um número inteiro.")

    def atualizar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        for produto in ProdutoController.listar_produtos():
            self.tabela.insert("", "end", values=(produto["id"], produto["nome"], f'R$ {produto["preco"]:.2f}', produto["estoque"]))
