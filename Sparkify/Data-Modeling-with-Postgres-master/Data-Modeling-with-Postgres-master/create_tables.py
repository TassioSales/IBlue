import psycopg2
from sql_queries import create_table_queries, drop_table_queries

config = {}
exec(open('config.py').read(), config)
user = config['user']
password = config['password']


def create_database():
    """ Função para criar banco de dados
    Args: 
        None.
    Returns: 
        Conn (obj): conexão com o banco de dados sparkify.
        Cur  (obj): cursor para executar consultas
        
    """

    # connect to default database
    conn = psycopg2.connect(f"host=127.0.0.1 dbname=student user={user} password={password}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect(f"host=127.0.0.1 dbname=sparkifydb user={user} password={password}")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """ Função para executar a consulta Drop Table.
    Args: 
        Conn (obj): conexão com o banco de dados sparkify.
        Cur  (obj): cursor para executar consultas.  
    Returns: 
        None.
        
    """

    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """ Função para executar consultas de tabelas.
    Args: 
        Conn (obj): conexão com o banco de dados sparkify
        Cur  (obj): cursor para executar consultas.  
    Returns: 
        None.
        
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ Função para chamar as funções create_database (), drop_tables () e create_tables ().
    Args: 
        None.  
    Returns: 
        None.
        
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
