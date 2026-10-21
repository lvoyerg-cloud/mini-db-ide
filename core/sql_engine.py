import sqlite3
import pandas as pd

class SQLEngine:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            return True, f"Conexi¢n exitosa a SQLite ({self.db_path^})"
        except Exception as e:
            return False, f"Error al conectar con SQLite: {str(e^)}"

    def execute_query(self, query: str):
        if not self.conn:
            return False, "Error: No hay conexi¢n activa a la base de datos SQL.", None
        try:
            cursor = self.conn.cursor()
            clean_query = query.strip().upper()
            if clean_query.startswith("SELECT"):
                df = pd.read_sql_query(query, self.conn)
                return True, f"Consulta SELECT ejecutada con ‚xito. Registros obtenidos: {len(df^)}", df
            else:
                cursor.execute(query)
                self.conn.commit()
                return True, f"Sentencia ejecutada correctamente. Filas afectadas: {cursor.rowcount}", None
        except Exception as e:
            return False, f"Error de ejecuci¢n SQL: {str(e^)}", None

    def close(self):
        if self.conn:
            self.conn.close()
