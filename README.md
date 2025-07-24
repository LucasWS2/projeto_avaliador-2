# 🏪 Sistema de Controle de Loja

Sistema desktop completo para controle de vendas em uma loja, com interface gráfica em **Tkinter**, arquitetura **MVC** e banco de dados **MySQL**. Projeto desenvolvido para fins acadêmicos, com organização profissional e funcionalidades reais.

---

## 🎯 Objetivo

Desenvolver um sistema desktop funcional para gerenciar uma loja, incluindo:
- Cadastro de clientes e produtos
- Registro de vendas com múltiplos itens
- Interface gráfica funcional e intuitiva
- Armazenamento e relacionamento dos dados via MySQL
- Estrutura em camadas (MVC) e boas práticas de código

---

## ⚙️ Funcionalidades

✅ Login de usuários com autenticação  
✅ Cadastro de clientes (nome, telefone, email)  
✅ Cadastro de produtos (nome, preço, estoque)  
✅ Registro de vendas (cliente, múltiplos produtos, quantidade, total)  
✅ Interface Tkinter com múltiplas janelas  
✅ Integração com banco de dados MySQL  
✅ Arquitetura organizada em **MVC**

---

## 🧱 Estrutura do Projeto

```
projeto_avaliador/
├── app/
│   ├── controllers/
│   ├── models/
│   ├── views/
│   ├── database/
│   └── main.py
├── docs/
│   ├── requisitos.txt
│   ├── algoritmo.txt
│   ├── modelo_banco.png
│   └── DER.png
├── README.md
└── .env
```

---

## 🗃 Banco de Dados

- Banco: `loja_db`
- Tabelas: `usuarios`, `clientes`, `produtos`, `vendas`, `itens_venda`
- Relacionamentos com chaves estrangeiras
- Diagrama ER incluso na pasta `/docs`

---

## 💻 Tecnologias Utilizadas

- Python 3
- Tkinter (interface gráfica)
- MySQL (armazenamento de dados)
- mysql-connector-python
- python-dotenv
- Git + GitHub

---

## ▶️ Como executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/LucasWS2/projeto_avaliador.git
   ```

2. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o arquivo `.env` com os dados do seu MySQL:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=
   DB_NAME=loja_db
   ```

5. Rode o projeto:
   ```bash
   python app/main.py
   ```

---

## 👨‍💻 Autor

Lucas Agostinho Wszoek