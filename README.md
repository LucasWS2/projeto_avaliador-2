
# Projeto Avaliador - Sistema de Controle de Loja

Sistema desenvolvido com Python e Tkinter para controle de clientes, produtos e vendas, utilizando MySQL como banco de dados.

## 🚀 Funcionalidades
- Cadastro e login de usuários
- Cadastro de clientes e produtos
- Registro e visualização de vendas

## ▶️ Como executar localmente

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/LucasWS2/projeto_avaliador-2.git
   ```

2. **Crie um ambiente virtual e ative**  
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `.env` com os dados do seu MySQL**  
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=
   DB_NAME=loja_db
   ```

5. **Crie o banco de dados**

   ### ✅ Opção 1 – Manual
   - Acesse o **phpMyAdmin**
   - Crie o banco `loja_db`
   - Importe o arquivo `docs/modelo_branco.sql`

   ### ⚙️ Opção 2 – Automática
   - Execute o script de setup:  
     ```bash
     python setup_db.py
     ```

     **Aviso:** Durante a execução, pode aparecer a seguinte mensagem:
     ```
     RuntimeError: generator raised StopIteration
     ```
     Isso é um comportamento conhecido do `mysql-connector` ao executar múltiplos comandos SQL.  
     **Pode ser ignorado com segurança**, pois o banco e as tabelas serão criados normalmente.

## 📂 Estrutura do Projeto Detalhada

```
projeto_avaliador-2/
│
├── app/
│   ├── controllers/        # Lógica da aplicação e regras de negócio
│   │   ├── cliente_controller.py
│   │   ├── produto_controller.py
│   │   ├── usuario_controller.py
│   │   └── venda_controller.py
│   │
│   ├── database/           # Conexão e configuração do banco de dados
│   │   └── conexao.py
│   │
│   ├── models/             # Modelos que representam e manipulam os dados
│   │   ├── cliente_model.py
│   │   ├── produto_model.py
│   │   ├── usuario_model.py
│   │   └── venda_model.py
│   │
│   └── views/              # Interfaces gráficas (Tkinter)
│       ├── cadastro_view.py
│       ├── cliente_view.py
│       ├── home_view.py
│       ├── login_view.py
│       ├── produto_view.py
│       ├── start_view.py
│       └── venda_view.py
│
├── docs/                   # Documentação e scripts auxiliares
│   ├── algoritmo.txt
│   ├── loja_db.pdf         # Diagrama ER do banco de dados
│   ├── modelo_branco.sql   # Script SQL para criar banco e tabelas
│   └── requisitos.txt
│
├── .env                    # Variáveis de ambiente para conexão ao banco
├── .gitignore              # Arquivos e pastas ignorados pelo Git
├── main.py                 # Ponto de entrada da aplicação
├── readme.md               # Documentação do projeto
└── setup_db.py             # Script para criar banco e tabelas automaticamente
```

## 💻 Tecnologias utilizadas

- Python 3  
- Tkinter (interface gráfica)  
- MySQL (banco de dados relacional)  
- mysql-connector-python (conector MySQL para Python)  
- python-dotenv (gerenciamento de variáveis de ambiente)  
- **bcrypt** (hash seguro de senhas)  
- Git e GitHub (controle de versão e hospedagem do código)  

## 👨‍💻 Autor
Lucas Agostinho Wszoek
