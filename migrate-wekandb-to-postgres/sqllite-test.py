import sqlite3

if __name__ == '__main__':
    print('Teste com SQlite')

    # Connect to sqlite database
    conn = sqlite3.connect('students.db')
    # cursor object
    cursor = conn.cursor()
    # drop query
    cursor.execute("DROP TABLE IF EXISTS STUDENT")
    # create query
    query = """CREATE TABLE if not exists STUDENT(
            ID INT PRIMARY KEY NOT NULL,
            NAME CHAR(20) NOT NULL, 
            ROLL CHAR(20), 
            ADDRESS CHAR(50), 
            CLASS CHAR(20) )"""
    cursor.execute(query)

    conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
             "VALUES (1, 'John', '001', 'Bangalore', '10th')")
    conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
             "VALUES (2, 'Naren', '002', 'Hyd', '12th')")

    

    # commit and close
    conn.commit()

    conn = sqlite3.connect('students.db')
    cursor = conn.execute("SELECT * from STUDENT")
    print(cursor.fetchall())

    conn.close()