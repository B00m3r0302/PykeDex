from rich import print

class CommandCapture:
    def __init__(self, command_input):
        self.input = command_input
        self.cleaned = None
        self.output = None

        self.clean_input()
        self.capture_first()

    def clean_input(self):
        try:
            clean_command = self.input.strip().lower()
            words = clean_command.split(' ')
            self.cleaned = [w for w in words if w != ' ']
        except Exception as e:
            print(F"Exception occurred: {e}")

    def capture_first(self):
        if not self.cleaned:
            self.output = None
            return

        self.output = self.cleaned[0]