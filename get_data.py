import httpx
import time
from pynput import keyboard
from rich.console import Console
from rich.prompt import Prompt
from rich import print

last_key = None
stop = False

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

def on_press(key):
    global last_key, stop

    if key == keyboard.Key.space:
        last_key = "space"
    elif key.char == "n":
        last_key = "n"
    elif key == keyboard.Key.esc:
        stop = True
        return False
    else:
        return "unsure"

def get_location_areas():
    global last_key, stop

    location_areas = []
    url = "location-area"

    Prompt("""
    Press <space> to show results
    Press <n> for the next page
    Press <esc> to stop and return to the main menu
    """)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while not stop:
        if last_key == "space":
            print("Showing page 1")
            response = make_request(url).json()
            for item in response["results"]:
                location_areas.append(item["name"])
            last_key = None
            yield location_areas
        elif last_key == "n":
            location_areas = []
            response = make_request(url).json()
            next_url = response.get("next")
            if next_url:
                # Extract just the endpoint part after the base URL
                url = next_url.replace("https://pokeapi.co/api/v2/", "")
                for item in response["results"]:
                    location_areas.append(item["name"])
                else:
                    url = None
                last_key = None
            yield location_areas
        elif last_key == "esc":
            break
        else:
            continue
    return

