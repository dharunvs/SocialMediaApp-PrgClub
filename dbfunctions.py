import sqlite3

def execute_query(sql_query):
    with sqlite3.connect("storage.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result

def add_post(name, message):
    sql_query = "INSERT INTO storage(name, message) VALUES('%s', '%s') " %(name, message)
    execute_query(sql_query)

def get_info():
    sql_query = "SELECT * FROM storage"
    result = execute_query(sql_query)
    return result.fetchall()

def delete_all():
    sql_query = "DELETE FROM storage"
    result = execute_query(sql_query)


