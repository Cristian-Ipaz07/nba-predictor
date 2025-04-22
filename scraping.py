import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.basketball-reference.com/leagues/NBA_2023_games.html"

response = requests.get(url)

if response.status_code == 200:
    games_df = pd.read_html(response.text)[0]
    print(games_df.head())
    games_df.to_csv('data/nba_games_2023.csv', index=False)
else:
    print(f"Error al obtener la página. Código de estado: {response.status_code}")
