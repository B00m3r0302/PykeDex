import sys
import get_data
from enum import Enum
from typing import Callable

class Command:
    def __init__(self, command, description, callback: Callable):
        self.command = command
        self.description = description
        self.callback = callback

def help_command(ctx):
    print("""
Welcome to the PykeDex!
Usage:


""")
    for cmd in Commands:
        c = cmd.value
        print(f"{c.command}: {c.description}")
    print()


def exit_command(ctx):
    print("Exiting the PykeDex!")
    sys.exit(0)

def map_command(ctx):
    location_areas = get_data.get_location_areas()
    for area in location_areas:
        print(area)

class Commands(Enum):
    HELP = Command(
        command = 'help',
        description = 'Show this help menu',
        callback = help_command,
    )
    EXIT = Command(
        command = 'exit',
        description = 'Exit the PykeDex',
        callback = exit_command,
    )
    MAP = Command(
        command = 'map',
        description = 'Show location areas',
        callback = map_command
    )

    @classmethod
    def from_input(cls, input_command):
        for cmd in cls:
            if cmd.value.command == input_command:
                return cmd
        return None
