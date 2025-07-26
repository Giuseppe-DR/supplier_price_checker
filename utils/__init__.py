import pandas as pd
import sqlite3

def db_to_excel(db_path, table_name, excel_path):
        # Connessione al database SQLite
        print("path db: " + db_path)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Carica la tabella in un DataFrame
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        # Esporta in Excel
        df.to_excel(excel_path, index=False)

        cursor.execute(f"DELETE FROM {table_name}")
        conn.commit()
        conn.close()