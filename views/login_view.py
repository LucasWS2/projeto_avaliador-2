import tkinter as tk
from tkinter import messagebox
from controllers.usuario_controller import UsuarioController
from views.home_view import HomeView

class LoginView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login - Sistema de Loja")
        self.root.geometry("300x200")

        tk.Label(self.root, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Senha:").pack(pady=5)
        self.senha_entry = tk.Entry(self.root, show="*")
        self.senha_entry.pack(pady=5)

        login_btn = tk.Button(self.root, text="Entrar", command=self.login)
        login_btn.pack(pady=10)

        self.root.mainloop()

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        usuario = UsuarioController.login(email, senha)

        if usuario:
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            self.root.destroy()
            HomeView(usuario["nome"])
        else:
            messagebox.showerror("Erro", "Email ou senha inválidos.")
