import requests
import argparse
import os
from dotenv import load_dotenv
from colorama import init, Fore
from tabulate import tabulate

init(autoreset=True) # Initialize coloroma

# Load APIkey
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY") or "PASTE_YOUR_API_KEY_HERE"

BASE_URL = "https://api.themoviedb.org/3/movie"

MOVIE_TYPES = {
    "playing": "now_playing",
    "popular": "popular",
    "top": "top_rated",
    "upcoming": "upcoming"
}

# Core Function
def fetch_movies(movie_type: str):
    if movie_type not in MOVIE_TYPES:
        print(Fore.RED + f"❌ Invalid type: '{movie_type}'. Must be one of {list(MOVIE_TYPES.keys())}")
        return

    url = f"{BASE_URL}/{MOVIE_TYPES[movie_type]}"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "page": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(Fore.RED + f"❌ Failed to fetch data: {response.status_code}")
        return

    data = response.json()
    results = data.get("results", [])

    if not results:
        print(Fore.YELLOW + "⚠️ No movies found.")
        return

    print(f"\n🎬 {Fore.CYAN + movie_type.upper()} MOVIES\n" + "=" * 60)

    table_data = []
    for i, movie in enumerate(results[:10], 1):
        title = movie.get("title", "N/A")
        rating = movie.get("vote_average", "N/A")
        release = movie.get("release_date", "N/A")
        table_data.append([f"{i}", title, release, f"{rating} ⭐"])

    headers = [Fore.YELLOW + "#", Fore.GREEN + "Title", Fore.MAGENTA + "Release Date", Fore.BLUE + "Rating"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

# CLI Argument Parsing
def main():
    parser = argparse.ArgumentParser(description="🎥 TMDB CLI Movie Fetcher")
    parser.add_argument("--type", type=str, required=True, help="Movie type: playing, popular, top, upcoming")
    args = parser.parse_args()
    fetch_movies(args.type.lower())

# Entry point
if __name__ == "__main__":
    main()