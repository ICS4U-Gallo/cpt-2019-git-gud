import arcade

import settings

from menu import MenuView
from load_file import LoadFile
from chapter_1 import Chapter1View
from chapter_2 import Chapter2View
from test_grid import Grid


class Director(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.view_index = 0
        self.views = [
            MenuView,
            LoadFile,
            Chapter1View,
            Chapter2View,
            Grid
            ]
        self.next_view()

    def next_view(self):
        next_view = self.views[self.view_index]()
        next_view.director = self
        self.show_view(next_view)
        self.view_index = (self.view_index + 1) % len(self.views)
    
    def specific_view(self, view):
        specific_view = view()
        specific_view.director = self
        self.show_view(specific_view)
        self.view_index = self.views.index(view)


def main():
    window = Director(settings.WIDTH, settings.HEIGHT, "CPT Structure")
    arcade.run()


if __name__ == "__main__":
    main()
