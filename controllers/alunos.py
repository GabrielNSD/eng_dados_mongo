from db.client import get_client

client = get_client()

db = client.ufrn_database
collection = db.alunos

'''
Retorna uma lista de items que possuem o campo com valor indicado na função
'''


def filtrar_alunos(campo, valor):
    return list(collection.find({campo: valor}, {'_id': False}))

'''
Pesquisa multi campo, recebe um dicionário como argumento. Esse dicionário contem os campos e seus respectivos valores a serem buscados
'''


def filtrar_alunos_multi_campo(search_dict):
    return list(collection.find(search_dict, {'_id': False}))
