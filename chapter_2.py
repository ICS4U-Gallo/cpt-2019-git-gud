import arcade

import settings

import os

import json


class Chapter2View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.selected_rect_x = 0
        self.selected_rect_y = 0
        self.pos_rect_x = 0
        self.pos_rect_y = 0
        self.characters = settings.CHARACTERS
        self.character_location = 0
        self.name = "  "

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("What's your name?", settings.WIDTH // 21,
                         settings.HEIGHT - settings.WIDTH // 25, arcade.color.WHITE,
                         30, 0, "left", 'Comic Sans', True, False, "left", "top")

        arcade.draw_rectangle_filled(settings.WIDTH // 2, settings.HEIGHT // 2.2,
                                     settings.WIDTH // 1.1, settings.HEIGHT // 1.25,
                                     arcade.color.WHITE)
        arcade.draw_rectangle_outline(settings.WIDTH // 2, settings.HEIGHT // 2.2,
                                      settings.WIDTH // 1.1,  settings.HEIGHT // 1.25,
                                      arcade.color.BLACK, 5)

        arcade.draw_rectangle_outline(settings.WIDTH - 703 + self.selected_rect_x,
                                      settings.HEIGHT - 122 - self.selected_rect_y,
                                      (settings.WIDTH //
                                       1.1) // 6, (settings.HEIGHT // 2.2) // 4,
                                      arcade.color.GOLD, 5)

        arcade.draw_rectangle_outline(564,
                                      settings.HEIGHT - settings.WIDTH // 16,
                                      400, 75, arcade.color.BLACK, 5)

        arcade.draw_text(self.name, 345,
                         settings.HEIGHT - settings.WIDTH // 40,
                         arcade.color.GOLD, 50, 0, "left", 'Comic  Sans',
                         True, True, "left", "top")

        row = 0
        column = 0
        for i in range(len(self.characters)):
            if i != 0:
                if i % 6 == 0 and i != 0:
                    column += 1
                    row = 0
                else:
                    row += 1
            arcade.draw_text(self.characters[i], settings.WIDTH - 703 + row * 121.3,
                             settings.HEIGHT - 122 - column * 68.6,
                             arcade.color.BLACK, 14, align="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            if self.pos_rect_x != 5:
                self.selected_rect_x += 121.3
                self.pos_rect_x += 1
                self.character_location += 1
            elif self.pos_rect_y != 6:
                self.selected_rect_x = 0
                self.pos_rect_x = 0
                self.selected_rect_y += 68.6
                self.pos_rect_y += 1
                self.character_location += 1

        if key == arcade.key.LEFT:
            if self.pos_rect_x != 0:
                self.selected_rect_x -= 121.3
                self.pos_rect_x -= 1
                self.character_location -= 1
            elif self.pos_rect_y != 0:
                self.selected_rect_x = 121.3 * 5
                self.pos_rect_x = 5
                self.selected_rect_y -= 68.6
                self.pos_rect_y -= 1
                self.character_location -= 1

        if key == arcade.key.UP:
            if self.pos_rect_y != 0:
                self.selected_rect_y -= 68.6
                self.pos_rect_y -= 1
                self.character_location -= 6

        if key == arcade.key.DOWN:
            if self.pos_rect_y != 6:
                self.selected_rect_y += 68.6
                self.pos_rect_y += 1
                self.character_location += 6

        if key == arcade.key.BACKSPACE and len(self.name) > 2:
            self.name = self.name[:-1]

        if self.character_location == 41 and key == arcade.key.ENTER:
            file_num = len(os.listdir("saves"))+1
            info = {"Name": self.name, "Character": settings.CHAR}
            with open(f"saves\Journey {file_num}.json", "w") as f:
                json.dump(info, f, indent=4)
            self.director.next_view()
        elif key == arcade.key.ENTER and modifiers == 1 and len(self.name) < 13:
            self.name += self.characters[self.character_location].upper()
        elif key == arcade.key.ENTER and len(self.name) < 13:
            self.name += self.characters[self.character_location]


if __name__ == "__main__":
    """This section of code will allow you to run your View
    independently from the main.py file and its Director.

    You can ignore this whole section. Keep it at the bottom
    of your code.

    It is advised you do not modify it unless you really know
    what you are doing.
    """
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Chapter2View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
