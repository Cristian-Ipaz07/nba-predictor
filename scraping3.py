import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def scrape_season_dynamic(season):
    base_url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
    response = requests.get(base_url)

    print(f"\n📅 Scrapeando temporada {season} ...")

    if response.status_code != 200:
        print(f"❌ Error al acceder a la temporada {season}. Código de estado: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    month_links = soup.select('a[href^="/leagues/NBA"]')

     # Depuración: imprimir los enlaces encontrados
    print(f"Enlaces de meses encontrados: {[link['href'] for link in month_links]}")

    # Extraer los meses disponibles desde los links
    months = [link['href'].split('-')[-1].replace('.html', '') for link in month_links if 'games' in link['href']]

    print(f"🗓️ Meses detectados: {months}")

    all_games = []

    for month in months:
        url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games-{month}.html"
        print(f"🔗 Obteniendo datos de: {url}")
        res = requests.get(url)
        if res.status_code == 200:
            try:
                df = pd.read_html(res.text)[0]
                all_games.append(df)
            except Exception as e:
                print(f"⚠️ No se pudo leer tabla de {month} en {season}: {e}")
        else:
            print(f"❌ No se pudo acceder a: {url}")

    if all_games:
        season_df = pd.concat(all_games)

        save_path = f"data/raw/nba_{season}.csv"
        season_df.to_csv(save_path, index=False)
        print(f"✅ Temporada {season} guardada en: {save_path}")
    else:
        print(f"⚠️ No se extrajo ningún dato para la temporada {season}")

if __name__ == "__main__":
    for season in range(2024, 2026):
        print("===========================")
        scrape_season_dynamic(season)
