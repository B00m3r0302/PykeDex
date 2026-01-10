from rich.console import Console
from rich import print
import typer

app = typer.Typer()

def tui_prompt():
    console = Console()
    console.input("[bold yellow]PykeDex>[/]")

def clean_input(command):
    clean_command = command.strip().lower()
    words = clean_command.split(" ")
    clean_command = [w for w in words if w != ""]
    return clean_command

@app.command()
def help():
    print("")
