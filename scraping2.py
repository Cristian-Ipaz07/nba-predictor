import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def scrape_season(season_year):
    print(f"\n📅 Scrapeando temporada {season_year} ...\n")
    url = f"https://www.basketball-reference.com/leagues/NBA_{season_year}_games.html"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌Error al acceder a la temporada {season_year}")

    soup = BeautifulSoup(response.text, "html.parser")
    month_links = soup.select("div.filter a")

    all_games = []

    for link in month_links:
        month_url = "https://www.basketball-reference.com" + link['href']
        print(f"Obteniendo datos de: {month_url}")
        mont_resp = requests.get(month_url)

        if mont_resp.status_code == 200:
            try:
                df = pd.read_html(mont_resp.text)[0]
                all_games.append(df)
            except ValueError:
                print(f"⚠️ No se encontro tabla en: {month_url}")

        else:
            print(f"⚠️ Error al cargar: {month_url}")

    if not all_games:
        print("⚠️ No se Extrajo ningun dato")
        return None
    
    full_season_df = pd.concat(all_games, ignore_index=True)

    raw_dir = os.path.join("data", "raw")
    csv_path = os.path.join(raw_dir, f"nba_{season_year}.csv")
    full_season_df.to_csv(csv_path, index=False)
    print(f"\n Temporada {season_year} guardada en: {csv_path}")

if __name__ == "__main__":
    print("ejecutando")
    for season in range(2015, 2025):
        print(f"===========================")
        print(f"Scrapeando temporada {season}")
        print(f"===========================")
        try:
            scrape_season(season)
        except Exception as e:
            print(f"❌ Error en la temporada {season}: {e}")

