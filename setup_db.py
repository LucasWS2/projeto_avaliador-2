from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

try:
    conn = connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    if conn.is_connected():
        print("✅ Conectado ao MySQL")
        cursor = conn.cursor()

        # Lê o conteúdo do arquivo SQL
        with open("docs/modelo_branco.sql", "r", encoding="utf-8") as f:
            sql_script = f.read()

        # Executa múltiplos comandos SQL
        print("🚀 Executando script SQL...")
        for comando in cursor.execute(sql_script, multi=True):
            if comando.with_rows:
                comando.fetchall()  # evita StopIteration em alguns casos

        print("✅ Banco de dados e tabelas criados com sucesso!")

        cursor.close()
        conn.close()

except Error as e:
    print("❌ Erro ao executar o script:", e)

except Exception as ex:
    print("❌ Erro inesperado:", ex)
