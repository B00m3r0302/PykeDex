import httpx
import time
from rich.console import Console

def make_request(endpoint):
    url = "https://pokeapi.co/api/v2/"
    new_url = url + endpoint
    res = httpx.get(new_url)
    progress_bar(new_url)
    return res

def progress_bar(url):
    console = Console()
    start = time.time()
    with console.status("[bold green]Fetching…"):
        res = httpx.get(url)
        elapsed = time.time() - start
        if elapsed < 0.7:
            time.sleep(0.7 - elapsed)

def get_location_areas():
    location_areas = []
    url = "location-area"

    while url:
        response = make_request(url).json()
        for item in response["results"]:
            location_areas.append(item["name"])

        # Get the next page URL, or None if we're done
        next_url = response.get("next")
        if next_url:
            # Extract just the endpoint part after the base URL
            url = next_url.replace("https://pokeapi.co/api/v2/", "")
        else:
            url = None

    return location_areas