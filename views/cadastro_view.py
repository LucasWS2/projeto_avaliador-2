import tkinter as tk
from tkinter import messagebox
from controllers.usuario_controller import UsuarioController
from views.login_view import LoginView

class CadastroView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro - Sistema de Loja")
        self.root.geometry("300x250")

        tk.Label(self.root, text="Nome:").pack(pady=5)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack(pady=5)

        tk.Label(self.root, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Senha:").pack(pady=5)
        self.senha_entry = tk.Entry(self.root, show="*")
        self.senha_entry.pack(pady=5)

        cadastrar_btn = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        cadastrar_btn.pack(pady=10)

        self.root.mainloop()

    def cadastrar(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if not nome or not email or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        sucesso = UsuarioController.cadastrar_usuario(nome, email, senha)

        if sucesso:
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.root.destroy()
            LoginView()
        else:
            messagebox.showerror("Erro", "Falha ao cadastrar. Verifique os dados e tente novamente.")
