from asyncio import start_unix_server
from functools import total_ordering
import get_data
import tui
import input
import commands
import typer

def main():
    while True:
        user_input = tui.tui_prompt()

        # Parse the input
        captured = input.CommandCapture(user_input)

        # Find and execute the command
        cmd = commands.Commands.from_input(captured.output)
        if cmd:
            cmd.value.callback(None)
        else:
            if captured.output:
                print(f"Unknown command: {captured.output}")

if __name__ == "__main__":
    typer.run(main())

