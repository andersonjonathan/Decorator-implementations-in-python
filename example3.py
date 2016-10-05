from contextlib import contextmanager


class Window:
    def __init__(self):
        self._content = 'text here'

    def draw(self, end=''):
        print(self._content, end=end)

    def get_content_width(self):
        return len(self._content)

    def info(self):
        pass


@contextmanager
def border_decorator(window):
    print('+-' + '-' * window.get_content_width() + '-+')
    print('| ', end='')
    yield
    print(' |')
    print('+-' + '-' * window.get_content_width() + '-+')


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
