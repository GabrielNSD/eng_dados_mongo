from db.client import get_client
import pandas as pd

client = get_client()

df = pd.read_csv('./db/data.csv', sep=';')

df_dict = df.to_dict(orient='records')


def populate():
    print("starting")
    db = client.ufrn_database
    collection = db.alunos
    collection.insert_many(df_dict)
    print("Done")