
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

## 🧠 Tecnologias utilizadas
- Python
- Tkinter
- MySQL
- mysql-connector-python
- python-dotenv

## 📁 Organização do projeto
```
projeto_avaliador-2/
│
├── controllers/
│   └── ... (lógica de controle de clientes, produtos e vendas)
├── models/
│   └── ... (interação com o banco de dados)
├── views/
│   └── ... (interfaces gráficas com Tkinter)
├── docs/
│   └── modelo_branco.sql
├── .env
├── setup_db.py
├── main.py
└── requirements.txt
```

## 👨‍💻 Autor
Lucas Agostinho Wszoek
