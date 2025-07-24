import tkinter as tk
from tkinter import ttk, messagebox
from controllers.venda_controller import VendaController
from controllers.cliente_controller import ClienteController
from controllers.produto_controller import ProdutoController

class VendaView:
    def __init__(self):
        self.itens = []

        self.root = tk.Toplevel()
        self.root.title("Registrar Venda")
        self.root.geometry("500x600")

        # Cliente
        tk.Label(self.root, text="Cliente:").pack()
        self.clientes = ClienteController.listar_clientes()
        self.cliente_cb = ttk.Combobox(self.root, values=[f"{c['id']} - {c['nome']}" for c in self.clientes])
        self.cliente_cb.pack(pady=5)

        # Produto
        tk.Label(self.root, text="Produto:").pack()
        self.produtos = ProdutoController.listar_produtos()
        self.produto_cb = ttk.Combobox(self.root, values=[f"{p['id']} - {p['nome']} - R$ {p['preco']:.2f}" for p in self.produtos])
        self.produto_cb.pack(pady=5)

        tk.Label(self.root, text="Quantidade:").pack()
        self.quantidade_entry = tk.Entry(self.root)
        self.quantidade_entry.pack(pady=5)

        tk.Button(self.root, text="Adicionar Item", command=self.adicionar_item).pack(pady=10)

        self.lista_itens = ttk.Treeview(self.root, columns=("Produto", "Qtd", "Preço Unit.", "Subtotal"), show="headings")
        self.lista_itens.heading("Produto", text="Produto")
        self.lista_itens.heading("Qtd", text="Qtd")
        self.lista_itens.heading("Preço Unit.", text="Preço Unit.")
        self.lista_itens.heading("Subtotal", text="Subtotal")
        self.lista_itens.pack(pady=10, fill=tk.BOTH, expand=True)

        self.total_var = tk.StringVar(value="Total: R$ 0.00")
        tk.Label(self.root, textvariable=self.total_var, font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self.root, text="Finalizar Venda", command=self.finalizar_venda).pack(pady=10)

    def adicionar_item(self):
        idx = self.produto_cb.current()
        if idx == -1:
            return messagebox.showerror("Erro", "Selecione um produto.")

        try:
            qtd = int(self.quantidade_entry.get())
            if qtd <= 0:
                raise ValueError
        except ValueError:
            return messagebox.showerror("Erro", "Quantidade inválida.")

        produto = self.produtos[idx]
        subtotal = produto["preco"] * qtd

        self.itens.append({
            "produto_id": produto["id"],
            "quantidade": qtd,
            "preco_unitario": produto["preco"]
        })

        self.lista_itens.insert("", "end", values=(produto["nome"], qtd, f"R$ {produto['preco']:.2f}", f"R$ {subtotal:.2f}"))
        self.quantidade_entry.delete(0, tk.END)
        self.atualizar_total()

    def atualizar_total(self):
        total = sum(item["preco_unitario"] * item["quantidade"] for item in self.itens)
        self.total_var.set(f"Total: R$ {total:.2f}")

    def finalizar_venda(self):
        idx = self.cliente_cb.current()
        if idx == -1:
            return messagebox.showerror("Erro", "Selecione um cliente.")
        if not self.itens:
            return messagebox.showerror("Erro", "Adicione pelo menos um item.")

        cliente_id = self.clientes[idx]["id"]
        total = sum(item["preco_unitario"] * item["quantidade"] for item in self.itens)

        VendaController.registrar(cliente_id, self.itens, total)
        messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
        self.root.destroy()
