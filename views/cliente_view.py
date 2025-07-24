import tkinter as tk
from tkinter import messagebox, ttk
from controllers.cliente_controller import ClienteController

class ClienteView:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Cadastro de Clientes")
        self.root.geometry("400x400")

        # Formulário
        tk.Label(self.root, text="Nome:").pack()
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack()

        tk.Label(self.root, text="Telefone:").pack()
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack()

        tk.Label(self.root, text="Email:").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        tk.Button(self.root, text="Cadastrar", command=self.cadastrar_cliente).pack(pady=10)

        # Tabela de clientes
        self.tabela = ttk.Treeview(self.root, columns=("ID", "Nome", "Telefone", "Email"), show="headings")
        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Telefone", text="Telefone")
        self.tabela.heading("Email", text="Email")
        self.tabela.pack(pady=10, fill=tk.BOTH, expand=True)

        self.atualizar_tabela()

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()

        if nome:
            ClienteController.cadastrar(nome, telefone, email)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.nome_entry.delete(0, tk.END)
            self.telefone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.atualizar_tabela()
        else:
            messagebox.showwarning("Erro", "O campo nome é obrigatório.")

    def atualizar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        for cliente in ClienteController.listar_clientes():
            self.tabela.insert("", "end", values=(cliente["id"], cliente["nome"], cliente["telefone"], cliente["email"]))
