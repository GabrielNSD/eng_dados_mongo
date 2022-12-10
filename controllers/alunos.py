from db.client import get_client

client = get_client()

db = client.ufrn_database
collection = db.alunos

def filtrar_alunos(campo, valor):
    return list(collection.find({campo: valor}, {'_id': False}))

def filtrar_alunos_multi_campo(search_dict):
    # search_dict = {}
    # for index in range(0,len(campos)-1):
    #     search_dict[campos[index]] = valores[index]
    
    return list(collection.find(search_dict, {'_id': False}))

