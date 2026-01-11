from rich.console import Console
import typer

app = typer.Typer()

def tui_prompt():
    console = Console()
    command = console.input("[bold yellow]PykeDex>[/]")
    return command

