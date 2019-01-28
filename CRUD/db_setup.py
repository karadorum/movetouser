import sqlite3
from sqlite3 import Error



database = "D:\Защита информации\DEV\CRUD\\testdb.db"

def create_connection(database):
    try:
        conn = sqlite3.connect(database)
            
    except Error as e:
        print(e)
        return None
    finally:
        return conn


def close_connection(conn):
    try:
        conn.close()
    except Error as e:
        print(e)


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def show_data(conn):
    try:
        query = 'SELECT rowid, * FROM items'
        c = conn.cursor()
        response = c.execute(query)
        
        #for item, url in response:
            #return item, url
    
    except Error as e:
        print(e)
    print( [(rowid, item, url) for rowid, item,url in response] )
        #for row_number, row in response:
            #for column, data in row:
            #print('1', item, '2', url)

    #
        
def show_rowid(conn):
    query = 'SELECT rowid FROM items'
    c = conn.cursor()
    response = c.execute(query)
    for rowid in response:
        print(rowid)
                
        


def insert_data(conn, param1, param2):
    
    try:
        query = 'INSERT INTO items (item, url) VALUES ({}, {})'.format(param1, param2)
        c = conn.cursor()
        conn.execute(query)
        conn.commit()
    except Error as e:
        print(e)


#def update_row(conn, ):
    
    

def main():
    
    database = "D:\Защита информации\DEV\CRUD\\testdb.db"
    sql_create_items_table = "CREATE TABLE IF NOT EXISTS items (item text NOT NULL, url text);"
    conn = create_connection(database)    
    #create_table(conn, sql_create_items_table)
    #insert_data(conn)
    show_rowid(conn)
    show_data(conn)
    close_connection(conn)


    


if __name__ == "__main__":
    main()

    