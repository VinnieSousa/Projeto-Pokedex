import pandas as pd
import requests
import sqlite3
from plyer import notification
from datetime import datetime

def save_to_db(df, table_name, conn):
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Tabela {table_name} salva no banco de dados")

url = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(url)

if response.status_code == 200:
    data_json = response.json()
    print("Funcionou")

    pokemon_list = []
    for pokemon in data_json['results']:
        pokemon_url = pokemon['url']
        pokemon_response = requests.get(pokemon_url)
        pokemon_data = pokemon_response.json()
        pokemon_info = {
            'name': pokemon_data['name'],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'base_experience': pokemon_data['base_experience']
            }
        pokemon_list.append(pokemon_info)
    df_pokemons = pd.DataFrame(pokemon_list)
    print(df_pokemons)
else:
    print("Não foi")

url = "https://pokeapi.co/api/v2/machine"
response = requests.get(url)

if response.status_code == 200:
    data_json = response.json()
    print("Funcionou")

    machine_list = []
    for machine in data_json['results']:
        machine_url = machine['url']
        machine_response = requests.get(machine_url)
        machine_data = machine_response.json()
        machine_info = {
             'id': machine_data['id'],
             'TM': machine_data['item']['name'],
             'generation': machine_data['version_group']['name'],
             'move': machine_data['move']['name'],

            }
        machine_list.append(machine_info)
    df_machine_list = pd.DataFrame(machine_list)
    print(df_machine_list)
else:
    print("Não foi")

url = "https://pokeapi.co/api/v2/move"
response = requests.get(url)

if response.status_code == 200:
    data_json = response.json()
    print("funcionou")

    move_list = []
    for move in data_json ['results']:
        move_url = move['url']
        move_response = requests.get(move_url)
        move_data = move_response.json()
        move_info = {
            'name': move_data ['name'],
            'type': move_data ['type']['name'],
            'power': move_data['power'],
            'accuracy': move_data['accuracy'],
            'power points': move_data['pp'],
            'effect': move_data ['effect_entries'][0]['short_effect'],
        }
        move_list.append(move_info)
    df_moves = pd.DataFrame(move_list)
    print(df_moves)
else:
    print("nao funcionou")

conn = sqlite3.connect('coderhouse.db')
save_to_db(df_pokemons, 'Pokemon', conn)
conn.close()

conn = sqlite3.connect('coderhouse.db')
save_to_db(df_machine_list, 'TMs', conn)
conn.close()

conn = sqlite3.connect('coderhouse.db')
save_to_db(df_moves, 'Moves', conn)
conn.close()

def alerta(nivel, base, etapa):
    now = str(datetime.now())
    msg = f"Falha no carregamento da base {base} na etapa {etapa}.\n{now}"

    if nivel == 1:
        title = 'ATENÇÃO: Alerta Baixo'
    elif nivel == 2:
        title = 'ATENÇÃO: Alerta Médio'
    elif nivel  == 3:
        title = 'ATENÇÃO: Alerta Alto'
    else:
        print("Nivel",nivel,"não disponível!")

    notification.notify(
            title=title,
            message=msg,
            app_name='alerta',
            timeout=10
        )

alerta(nivel = 3,
        base = "POKEDEX", 
        etapa = "EXTRACAO")

conn = sqlite3.connect('coderhouse.db')
query = "SELECT * FROM Pokemon"
df = pd.read_sql(query, conn)
print(df)

conn.close()

conn = sqlite3.connect('coderhouse.db')
query = "SELECT name FROM sqlite_master WHERE type='table'"
schema = pd.read_sql_query(query, conn)
print(schema)

conn.close()