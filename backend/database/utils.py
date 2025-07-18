import psycopg2, os, time # type: ignore
from psycopg2 import Error # type: ignore
from psycopg2.extras import RealDictCursor # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()
db_user = os.getenv("DB_User")
db_pass = os.getenv("DB_User_PASS")

def sqlQuery(sql: str, params: tuple, fetch: int = 0):
    while True:
        try:
            conn = psycopg2.connect(database='echoverse',user=db_user,password=db_pass,host='localhost',port='5432',cursor_factory=RealDictCursor)
            cur = conn.cursor()
            break
        except Error as e:
            if conn:
                conn.close()
            print(f"Error connecting to DB: {e}")
            time.sleep(5)
    try:
        if fetch > 1:
            cur.execute(f"{sql} LIMIT {fetch};",params)
            out = cur.fetchall()
        elif fetch == 1:
            cur.execute(f"{sql}",params)
            out = cur.fetchone()
        else:
            cur.execute(f"{sql}",params)
            out = None
    except Exception as e:
        print(e)
        raise 'sql error'
    conn.commit()
    conn.close()
    return out

