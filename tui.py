from rich.console import Console
from rich import print
import typer

app = typer.Typer()

def tui_prompt():
    console = Console()
    command = console.input("[bold yellow]PykeDex>[/]")

def clean_input(command):
    clean_command = command.strip().lower()
    words = clean_command.split(" ")
    clean_command = [w for w in words if w != ""]
    return clean_command

def capture_first_input(command):
    command = clean_input(command)
    first_word = command[0]
    return first_word

@app.command("help")
def pykedex_help():
    print("""
    Welcome to the Pykedex!
    Usage:
    
    
    help: displays a help message
    exit: exits the program
    """)
