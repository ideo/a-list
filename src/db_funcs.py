import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_tables(db_file: str):

    sql_create_docs_table = """ CREATE TABLE IF NOT EXISTS docs (
                                        id integer PRIMARY KEY,
                                        text text NOT NULL,
                                        leader_id integer,
                                        year integer,
                                        month integer,
                                        source text,
                                        FOREIGN KEY (leader_id) REFERENCES leaders (id)
                                    ); """

    sql_create_leaders_table = """CREATE TABLE IF NOT EXISTS leaders (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    org text NOT NULL
                                );"""

    # create a database connection
    conn = create_connection(db_file)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_docs_table)

        # create tasks table
        create_table(conn, sql_create_leaders_table)
    else:
        print("Error! cannot create the database connection.")





def load_examples(db_path):
    # create a database connection
    conn = create_connection(db_path)

    # # create tables
    # if conn is not None:
    #     # create projects table
    #     create_table(conn, sql_create_docs_table)

    #     # create tasks table
    #     create_table(conn, sql_create_leaders_table)
    # else:
    #     print("Error! cannot create the database connection.")