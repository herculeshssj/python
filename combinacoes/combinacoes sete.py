import mariadb
import itertools
import time

# Conectando ao banco de dados
conn_params= {
    "user" : "root",
    "password" : "root",
    "host" : "raspberrypi",
    "database" : "combinacoes"
}
conn = mariadb.connect(**conn_params)
cursor = conn.cursor()

# Criando a tabela
#cursor.execute("CREATE TABLE IF NOT EXISTS combinacoes (id INT AUTO_INCREMENT PRIMARY KEY)")
"""
Código original

-- combinacoes.combinacoes_sete definition

CREATE TABLE `combinacoes_sete` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `col1` int(11) DEFAULT NULL,
  `col2` int(11) DEFAULT NULL,
  `col3` int(11) DEFAULT NULL,
  `col4` int(11) DEFAULT NULL,
  `col5` int(11) DEFAULT NULL,
  `col6` int(11) DEFAULT NULL,
  `col7` int(11) DEFAULT NULL,
  `conjunto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
"""

# Gerando todas as combinações possíveis de 7 números de 1 a 31 sem repetição
combinacoes = list(itertools.combinations(range(1, 32), 7))

# Inserindo as combinações na tabela
for i, combinacao in enumerate(combinacoes):
    #print(i)
    print(combinacao)
    #time.sleep(1)

    #commit_count = 0

    query_string = "INSERT INTO combinacoes.combinacoes_sete (col1, col2, col3, col4, col5, col6, col7, conjunto) VALUES({}, {}, {}, {}, {}, {}, {}, '{}')"
    tupla_string = ', '.join(str(elemento) for elemento in combinacao)
    query = query_string.format(combinacao[0],combinacao[1],combinacao[2],combinacao[3],combinacao[4],combinacao[5],
                                combinacao[6],tupla_string)
    
    cursor.execute(query)
    conn.commit()

    #commit_count += 1
"""
    if commit_count == 10000:
        conn.commit()
        commit_count = 0
        print('Commit!')


    query = "ALTER TABLE combinacoes ADD COLUMN col{} INT".format(i+1)
    print(query)
    cursor.execute(query)

    query = "INSERT INTO combinacoes (id) VALUES ({})".format(i+1)
    print(query)
    cursor.execute(query)

    for j, numero in enumerate(combinacao):
        query = "UPDATE combinacoes SET col{} = {} WHERE id = {}".format(j+1, numero, i+1)
        print(query)
        cursor.execute(query)

    """
#conn.commit()
conn.close()