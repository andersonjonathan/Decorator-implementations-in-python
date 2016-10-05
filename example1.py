class Window:
    def __init__(self):
        self._content = 'text here'

    def draw(self, end='\n'):
        print(self._content, end=end)

    def get_content_width(self):
        return len(self._content)

    def info(self):
        pass


class BorderDecorator:
    def __init__(self, w):
        self._window = w

    def draw(self):
        print('+-' + '-' * self._window.get_content_width() + '-+')
        print('| ', end='')
        self._window.draw(end='')
        print(' |')
        print('+-' + '-' * self._window.get_content_width() + '-+')

    def get_content_width(self):
        return self._window.get_content_width()

    def info(self):
        self._window.info()


def main():
    window = Window()
    w = BorderDecorator(window)

    w.draw()
    # Output:
    # +-----------+
    # | text here |
    # +-----------+

    window.draw()
    # Output:
    # text here

if __name__ == '__main__':
    main()
