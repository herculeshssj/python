import sqlite3

if __name__ == '__main__':
    print('SQLite 3')

    conexao = sqlite3.connect('basededados.db')

    cursor = conexao.cursor()

    cursor.execute(
        'create table if not exists clientes (id integer primary key autoincrement, nome text, peso real)')

    cursor.execute(
        'insert into clientes (nome, peso) values (?, ?)', ('João', 80))
    cursor.execute(
        'insert into clientes (nome, peso) values (:nome, :peso)', {'nome': 'Maria', 'peso': 60})
    cursor.execute(
        'insert into clientes values (:id, :nome, :peso)', {'id': None, 'nome': 'Daniel', 'peso': 130})
    conexao.commit()

    cursor.execute('select * from clientes')
    for linha in cursor.fetchall():
        # print(linha)
        ident, nome, peso = linha
        print(ident, nome, peso)

    cursor.execute('update clientes set nome = :nome where id = :id', {
                   'id': 2, 'nome': 'Joana'})
    conexao.commit()

    cursor.execute('select * from clientes')
    for linha in cursor.fetchall():
        # print(linha)
        ident, nome, peso = linha
        print(ident, nome, peso)

    cursor.execute('delete from clientes where id = :id', {'id': 3})
    conexao.commit()

    cursor.execute('select * from clientes')
    for linha in cursor.fetchall():
        # print(linha)
        ident, nome, peso = linha
        print(ident, nome, peso)

    cursor.close()
    conexao.close()
