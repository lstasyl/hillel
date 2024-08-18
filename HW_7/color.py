class colorizer:
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'reset': '\033[0m'
    }

    def __init__(self, color):
        self.color = color

    def __enter__(self):
        print(self.colors.get(self.color, self.colors['reset']), end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.colors['reset'], end='')


with colorizer('cyan'):
    print('printed in red')
print('printed in default color')
