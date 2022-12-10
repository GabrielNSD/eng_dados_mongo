# Prática MongoDB  

Esta prática consiste na criação e consumo de um banco de dados em MongoDB.
  
## Executando a aplicação  

1 - Inicie os containers com `docker-compose up`

Executando pela primeira vez:  
2 - Salve o arquivo `discentes-2022.csv` no diretório `db`.  
3 - Entre no terminal do container `alunos-api`, utilizando `docker exec -it alunos-api /bin/bash`.  
4 - Popule o banco de dados com o comando `python populate.py`
  
Após esses passos a API estará pronta para consultas.  

## Consultado a API
  
A API pode ser acessada pelo endereço: `http://localhost:5002`  
  
Com as seguinte rotas

### /ingressaram-sisu  
> Retorna todos os alunos que ingressaram por meio do SiSU

### /ingressaram-mestrado  
> Retorna todos os alunos que ingressaram em um programa de mestrado
  
### /alunos-unidade?unidade=nome_unidade
> Retorna todos os alunos de uma unidade, indicado pelo parâmetro `unidade` na query.  
> Ex.: /alunos-unidade?unidade=CENTRO%20DE%20TECNOLOGIA  
  
### /alunos-regulares  
> Retorna todos os alunos regulares
  
### /alunos-por-status?status=status
> Retorna todos os alunos que possuem o status indicado pelo parâmetro `status`.  
> Ex.: /alunos-por-status?status=ATIVO