import types


class Window:
    def __init__(self):
        self._content = 'text here'

    def draw(self, end=''):
        print(self._content, end=end)

    def get_content_width(self):
        return len(self._content)

    def info(self):
        pass


def border_decorator(target):
    def draw(self):
        print('+-' + '-' * self.get_content_width() + '-+')
        print('| ', end='')
        self.__internal_draw()
        print(' |')
        print('+-' + '-' * self.get_content_width() + '-+')

    setattr(target, '__internal_draw', target.draw)
    target.draw = types.MethodType(draw, target)


def remove_border_decorator(target):
    setattr(target, 'draw', target.__internal_draw)


def main():
    window = Window()
    border_decorator(window)

    window.draw()
    # Output:
    # +-----------+
    # | text here |
    # +-----------+

    remove_border_decorator(window)

    window.draw()
    # Output:
    # text here

if __name__ == '__main__':
    main()
