class Window:
    def __init__(self):
        self._content = 'text here'

    def draw(self, end=''):
        print(self._content, end=end)

    def get_content_width(self):
        return len(self._content)

    def info(self):
        pass


class border_decorator:
    def __init__(self, window):
        self._window = window

    def __enter__(self):
        print('+-' + '-' * self._window.get_content_width() + '-+')
        print('| ', end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(' |')
        print('+-' + '-' * self._window.get_content_width() + '-+')


def main():
    window = Window()

    with border_decorator(window):
        window.draw()
    # Output:
    # +-----------+
    # | text here |
    # +-----------+

    window.draw()
    # Output:
    # text here

if __name__ == '__main__':
    main()
