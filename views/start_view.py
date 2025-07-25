import tkinter as tk
from views.login_view import LoginView
from views.cadastro_view import CadastroView

class StartView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bem-vindo")
        self.root.geometry("300x150")

        tk.Label(self.root, text="Escolha uma opção", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Login", width=15, command=self.abrir_login).pack(pady=5)
        tk.Button(self.root, text="Cadastrar", width=15, command=self.abrir_cadastro).pack(pady=5)

        self.root.mainloop()

    def abrir_login(self):
        self.root.destroy()
        LoginView()

    def abrir_cadastro(self):
        self.root.destroy()
        CadastroView()
