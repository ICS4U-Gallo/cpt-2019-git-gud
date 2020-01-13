import arcade
import settings
import utils
import os
import json
from test_grid import Grid


class LoadFile(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLUEBERRY)
        self.saves = {0: None, 1: None, 2: None}
        for i in range(len(os.listdir("saves"))):
            self.saves[i] = os.listdir("saves")[i]

        self.file_indicator = settings.HEIGHT//2 + 192
        self.selection = 0
        self.selected = False
        self.confirmation = True
        self.confirmation_indicator = {
            "YES": arcade.color.GOLD, "NO": arcade.color.BLACK}

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Load File", settings.WIDTH // 20,
                         settings.HEIGHT - settings.WIDTH // 25, arcade.color.WHITE,
                         30, 0, "left", 'Comic Sans', True, False, "left", "top")

        arcade.draw_rectangle_filled(
            settings.WIDTH//2, settings.HEIGHT//2 + 30, 500, 360, arcade.color.ASH_GREY)

        for i in range(3):
            arcade.draw_rectangle_outline(
                settings.WIDTH//2, settings.HEIGHT//2 + 150 - i * 120,
                500, 120, arcade.color.BLACK, border_width=3)
            if self.saves[i] is not None:
                arcade.draw_text(f"Journey {i + 1}", settings.WIDTH//2 - 240, settings.HEIGHT //
                                 2 + 200 - i * 120, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")
            else:
                arcade.draw_text("Empty", settings.WIDTH//2 - 240, settings.HEIGHT//2 +
                                 200 - i * 120, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")

        arcade.draw_rectangle_outline(
            settings.WIDTH//2 - 206, self.file_indicator, 76, 20, arcade.color.GOLD, border_width=2)
        arcade.draw_rectangle_filled(
            settings.WIDTH//2, 60, settings.WIDTH, 120, arcade.color.WHITE)
        arcade.draw_rectangle_outline(
            settings.WIDTH//2, 60, settings.WIDTH - 3, 120, arcade.color.BLACK, 3)

        if not self.selected:
            arcade.draw_text("Use arrow keys to choose file slot...", 60,
                             80, arcade.color.BLACK, 14, anchor_x="left", anchor_y="center")
            arcade.draw_text("Press the enter key to select...", 60, 40,
                             arcade.color.BLACK, 14, anchor_x="left", anchor_y="center")
        else:
            if self.saves[self.selection] is None:
                arcade.draw_text(f"Create new save file?", 60, 80,
                                 arcade.color.BLACK, 14, anchor_x="left", anchor_y="center")
            else:
                arcade.draw_text(f"Load 'Journey {self.selection}'?", 60, 80,
                                 arcade.color.BLACK, 14, anchor_x="left", anchor_y="center")

            arcade.draw_rectangle_outline(
                700, 80, 80, 40, arcade.color.BLACK, 2)
            arcade.draw_rectangle_outline(
                700, 40, 80, 40, arcade.color.BLACK, 2)
            arcade.draw_text(
                "Y E S", 700, 80, self.confirmation_indicator["YES"], 18, anchor_x="center", anchor_y="center")
            arcade.draw_text(
                "N O", 700, 40, self.confirmation_indicator["NO"], 18, anchor_x="center", anchor_y="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.selected:
                self.confirmation = True
                self.confirmation_indicator = {
                    "YES": arcade.color.GOLD, "NO": arcade.color.BLACK}
            elif self.selection > 0:
                self.file_indicator += 120
                self.selection -= 1

        if key == arcade.key.DOWN:
            if self.selected:
                self.confirmation = False
                self.confirmation_indicator = {
                    "YES": arcade.color.BLACK, "NO": arcade.color.GOLD}
            elif self.selection < 2:
                self.file_indicator -= 120
                self.selection += 1

        if key == arcade.key.ENTER:
            if not self.selected:
                self.selected = True
            else:
                if self.confirmation is False:
                    self.selected = False
                    self.confirmation_indicator = {
                        "YES": arcade.color.GOLD, "NO": arcade.color.BLACK}
                    self.confirmation = True
                elif self.saves[self.selection] is None:
                    self.director.next_view()
                else:
                    with open(f"saves\{self.saves[self.selection]}", "r") as f:
                        settings.info = json.load(f)
                    self.director.specific_view(Grid)


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
    my_view = LoadFile()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
