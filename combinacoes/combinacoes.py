import mysql.connector
import itertools
import time

# Conectando ao banco de dados
conn = mysql.connector.connect(
    host="raspberrypi",
    user="root",
    password="root",
    database="combinacoes"
)
cursor = conn.cursor()

# Criando a tabela
#cursor.execute("CREATE TABLE IF NOT EXISTS combinacoes (id INT AUTO_INCREMENT PRIMARY KEY)")
"""
Código original

-- combinacoes.combinacoes definition

CREATE TABLE `combinacoes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `col1` int(11) DEFAULT NULL,
  `col2` int(11) DEFAULT NULL,
  `col3` int(11) DEFAULT NULL,
  `col4` int(11) DEFAULT NULL,
  `col5` int(11) DEFAULT NULL,
  `col6` int(11) DEFAULT NULL,
  `col7` int(11) DEFAULT NULL,
  `col8` int(11) DEFAULT NULL,
  `col9` int(11) DEFAULT NULL,
  `col10` int(11) DEFAULT NULL,
  `col11` int(11) DEFAULT NULL,
  `col12` int(11) DEFAULT NULL,
  `col13` int(11) DEFAULT NULL,
  `col14` int(11) DEFAULT NULL,
  `col15` int(11) DEFAULT NULL,
  `conjunto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
"""

# Gerando todas as combinações possíveis de 15 números de 1 a 25 sem repetição
combinacoes = list(itertools.combinations(range(1, 26), 15))

# Inserindo as combinações na tabela
for i, combinacao in enumerate(combinacoes):
    #print(i)
    #print(combinacao)
    #time.sleep(1)

    #commit_count = 0

    query_string = "INSERT INTO combinacoes.combinacoes (col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, conjunto) VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}')"
    tupla_string = ', '.join(str(elemento) for elemento in combinacao)
    query = query_string.format(combinacao[0],combinacao[1],combinacao[2],combinacao[3],combinacao[4],combinacao[5],
                                combinacao[6],combinacao[7],combinacao[8],combinacao[9],combinacao[10],combinacao[11],
                                combinacao[12],combinacao[13],combinacao[14],tupla_string)
    
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