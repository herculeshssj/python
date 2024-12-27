import random
import mariadb

def gerar_cpf():
    """Gera um CPF válido no formato 999.999.999-99"""
    def calc_digitos(cpf_base):
        """Calcula os dois dígitos verificadores do CPF"""
        for i in range(2):
            soma = sum(int(d) * (len(cpf_base) + 1 - j) for j, d in enumerate(cpf_base))
            digito = (soma * 10) % 11
            if digito == 10:
                digito = 0
            cpf_base.append(str(digito))
        return ''.join(cpf_base)

    cpf_base = [str(random.randint(0, 9)) for _ in range(9)]
    cpf_completo = calc_digitos(cpf_base)
    return f"{cpf_completo[:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:]}"

def conectar_e_atualizar_cpf():
    """Conecta ao banco de dados e atualiza os CPFs nas tabelas"""
    conn = None
    cursor = None
    try:
        # Conexão com o banco de dados
        conn = mariadb.connect(
            host='rockylinux',  # e.g., 'localhost' ou '127.0.0.1'
            user='root',
            password='root',
            database='cap'
        )
        cursor = conn.cursor()

        # Obtém todos os IDs da tabela users
        cursor.execute("SELECT id FROM users")
        ids = cursor.fetchall()

        # Atualiza a tabela users
        # Atualiza o CPF de cada registro
        for (id,) in ids:
            cpf = gerar_cpf()  # Gera um novo CPF para cada registro
            cursor.execute("UPDATE users SET cpf = %s WHERE id = %s", (cpf, id))

        cursor.execute("SELECT id FROM candidatos")
        ids = cursor.fetchall()

        # Atualiza a tabela candidatos
        for (id,) in ids:
            cpf = gerar_cpf()  # Gera um novo CPF para cada registro
            cursor.execute("UPDATE candidatos SET cpf = %s WHERE id = %s and cpf is not null", (cpf, id))

        # Confirma as alterações
        conn.commit()
        print("CPFs atualizados com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        # fecha o cursor e a conexão
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    conectar_e_atualizar_cpf()