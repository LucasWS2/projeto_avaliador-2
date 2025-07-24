import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.usuario_model import UsuarioModel

def main():
    nome = "Lucas"
    email = "lucas@email.com"
    senha = "123456"  # sem criptografia por enquanto

    UsuarioModel.criar_usuario(nome, email, senha)
    print(f"✅ Usuário '{nome}' criado com sucesso!")

if __name__ == "__main__":
    main()
