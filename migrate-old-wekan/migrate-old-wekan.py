from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

# Configurações da instância antiga
OLD_MONGO_URI = "mongodb://wekan:wekan@localhost:27017/wekan_old"
# Configurações da instância nova
NEW_MONGO_URI = "mongodb://wekan:wekan@localhost:27017/wekan"

def migrate_database(old_uri, new_uri):
    try:
        old_client = MongoClient(old_uri)
        new_client = MongoClient(new_uri)

        old_db = old_client.get_database()
        new_db = new_client.get_database()

        collections = old_db.list_collection_names()

        for coll_name in collections:
            print(f"Migrando coleção: {coll_name}")
            old_coll = old_db[coll_name]
            new_coll = new_db[coll_name]

            # Remove dados antigos da nova instância (opcional)
            #new_coll.delete_many({})

            # Copia documentos
            documents = list(old_coll.find({}))
            if documents:
                new_coll.insert_many(documents)
                print(f"→ {len(documents)} documentos migrados.")
            else:
                print("→ Nenhum documento encontrado.")

        print("\n✅ Migração concluída com sucesso!")

    except Exception as e:
        print(f"❌ Erro durante a migração: {e}")
        sys.exit(1)

if __name__ == "__main__":
    migrate_database(OLD_MONGO_URI, NEW_MONGO_URI)# Script de migração de dados do Wekan entre duas instâncias MongoDB