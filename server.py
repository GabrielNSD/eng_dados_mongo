from flask import Flask, request, json
from controllers.alunos import filtrar_alunos, filtrar_alunos_multi_campo
'''
1. Listar todos os alunos que ingressaram por meio do SiSU 
2. Listar todos os alunos que ingressaram no mestrado
3. Listar todos os alunos de uma unidade gestora
4. Listar todos os alunos regulares
5. Listar todos os alunos pelo status (cancelado, ativo, etc.)
'''

bad_url = "url mal formatada"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def home():
    return "Alunos 2022"


@app.route('/ingressaram-sisu', methods=['GET'])
def listar_sisu():
    return filtrar_alunos('forma_ingresso', 'SiSU')


@app.route('/ingressaram-mestrado', methods=['GET'])
def listar_mestrado():
    return filtrar_alunos_multi_campo({
        'forma_ingresso': 'SELEÇÃO DE PÓS-GRADUAÇÃO',
        'nivel_ensino': 'MESTRADO'
    })


@app.route('/alunos-unidade', methods=['GET'])
def alunos_unidade():
    args = request.args
    if len(args) == 0:
        return bad_url
    args_dict = args.to_dict()
    if 'unidade' in args_dict:
        return filtrar_alunos('nome_unidade_gestora', args_dict['unidade'])
    else:
        return bad_url


@app.route('/alunos-regulares', methods=['GET'])
def alunos_regulares():
    return filtrar_alunos('tipo_discente', 'REGULAR')


@app.route('/alunos-por-status', methods=['GET'])
def alunos_status():
    args = request.args
    if len(args) == 0:
        return bad_url
    args_dict = args.to_dict()
    if 'status' in args_dict:
        return filtrar_alunos('status', args_dict['status'])
    else:
        return bad_url


if __name__ == "__main__":
    app.run(host='0.0.0.0')