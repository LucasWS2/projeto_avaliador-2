import tkinter as tk
from tkinter import messagebox

class HomeView:
    def __init__(self, usuario_nome):
        self.root = tk.Tk()
        self.root.title("Sistema de Loja - Painel Principal")

        tk.Label(self.root, text=f"Bem-vindo, {usuario_nome}!", font=("Arial", 14)).pack(pady=10)

        btn_cliente = tk.Button(self.root, text="Cadastro de Clientes", width=30, command=self.ir_para_clientes)
        btn_cliente.pack(pady=5)

        btn_produto = tk.Button(self.root, text="Cadastro de Produtos", width=30, command=self.ir_para_produtos)
        btn_produto.pack(pady=5)

        btn_venda = tk.Button(self.root, text="Registrar Venda", width=30, command=self.ir_para_vendas)
        btn_venda.pack(pady=5)

        btn_sair = tk.Button(self.root, text="Sair", width=30, command=self.root.destroy)
        btn_sair.pack(pady=20)

        self.root.mainloop()

    def ir_para_clientes(self):
        messagebox.showinfo("Em breve", "Tela de cadastro de clientes em construção.")

    def ir_para_produtos(self):
        messagebox.showinfo("Em breve", "Tela de cadastro de produtos em construção.")

    def ir_para_vendas(self):
        messagebox.showinfo("Em breve", "Tela de registro de vendas em construção.")
