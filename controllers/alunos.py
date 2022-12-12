from db.client import get_client

client = get_client()

db = client.ufrn_database
collection = db.alunos


def filtrar_alunos(campo, valor):
    return list(collection.find({campo: valor}, {'_id': False}))


def filtrar_alunos_multi_campo(search_dict):
    return list(collection.find(search_dict, {'_id': False}))
