import json
from pymongo import MongoClient
import pandas as pd

class NoSQLEngine:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="ide_nosql_db"):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri, serverSelectionTimeoutMS=2000)
            self.client.admin.command('ping')
            self.db = self.client[self.db_name]
            return True, f"Conexion exitosa a MongoDB ({self.db_name^})"
        except Exception as e:
            return False, f"Error al conectar con MongoDB: {str(e^)}"

    def execute_command(self, collection_name: str, action: str, payload_json: str):
        if self.db is None:
            return False, "Error: No hay conexion activa a MongoDB.", None
        try:
            collection = self.db[collection_name]
            data = json.loads(payload_json) if payload_json.strip() else {}
            if action == "find":
                results = list(collection.find(data))
                for doc in results:
                    doc['_id'] = str(doc['_id'])
                df = pd.DataFrame(results)
                return True, f"Consulta NoSQL ejecutada. Documentos encontrados: {len(results^)}", df
            elif action == "insert_one":
                res = collection.insert_one(data)
                return True, f"Documento insertado correctamente con _id: {res.inserted_id}", None
            elif action == "delete_many":
                res = collection.delete_many(data)
                return True, f"Documentos eliminados: {res.deleted_count}", None
            elif action == "drop_collection":
                collection.drop()
                return True, f"Coleccion '{collection_name}' eliminada correctamente (DDL^).", None
            else:
                return False, f"Accion '{action}' no valida.", None
        except Exception as e:
            return False, f"Error en operacion NoSQL: {str(e^)}", None
