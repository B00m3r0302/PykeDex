from asyncio import start_unix_server
from functools import total_ordering
import get_data
import tui
import typer

def main():
    print(tui.clean_input('          hahahaha you       suck     man!'))
    while 1:
        tui.tui_prompt()

if __name__ == "__main__":
    typer.run(main())

