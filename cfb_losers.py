import pandas as pd
import networkx as nx
import json
import requests
import matplotlib as plt
import cfbd

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'YJ5gLZjtsR9KtIihcsBr50B+fdpMMkb2vPwmN+NSP1H8Iyf1a4x8d+LdBPe3CAHl'
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
games = api_instance.get_games(year=2021, conference='SEC')
response = requests.get(games)
json_data = json.loads(response.text)

df = pd.DataFrame(json_data)

graph = nx.Graph()

for team in df['team']:
    graph.add_node(team)

# Add edges for each game played during the regular season
for index, row in df.iterrows():
    if row['wins'] > row['losses']:
        winner = row['team']
        loser = row['opponent']
    else:
        winner = row['opponent']
        loser = row['team']
    graph.add_edge(winner, loser)

nx.draw(graph, with_labels=True)
plt.show()
