import arcade
import settings
import os
import json
from test_grid import Grid


class LoadFile(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLUEBERRY)

        if not settings.load_saves:
            self.saves = {0: None, 1: None, 2: None}
            for i in range(len(os.listdir("saves"))):
                self.saves[i] = os.listdir("saves")[i]
            settings.load_saves = True

        self.indicator_y = settings.HEIGHT//2 + 192
        self.selection = 0
                    

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Load File", settings.WIDTH // 20,
                         settings.HEIGHT - settings.WIDTH // 25, arcade.color.WHITE,
                         30, 0, "left", 'Comic Sans', True, False, "left", "top")

        arcade.draw_rectangle_filled(settings.WIDTH//2, settings.HEIGHT//2 + 150, 500, 120, arcade.color.ASH_GREY)
        arcade.draw_text(self.saves[0], settings.WIDTH//2 - 240, settings.HEIGHT//2 + 200, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")

        arcade.draw_rectangle_filled(settings.WIDTH//2, settings.HEIGHT//2 + 30, 500, 120, arcade.color.ASH_GREY)
        if self.saves[1] is None:
            arcade.draw_text("Empty", settings.WIDTH//2 - 240, settings.HEIGHT//2 + 80, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")
        else:
            arcade.draw_text(self.saves[1], settings.WIDTH//2 - 240, settings.HEIGHT//2 + 80, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")

        arcade.draw_rectangle_filled(settings.WIDTH//2, settings.HEIGHT//2 - 90, 500, 120, arcade.color.ASH_GREY)
        if self.saves[2] is None:
            arcade.draw_text("Empty", settings.WIDTH//2 - 240, settings.HEIGHT//2 - 40, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")
        else:
            arcade.draw_text(self.saves[1], settings.WIDTH//2 - 240, settings.HEIGHT//2 - 40, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")
        
        arcade.draw_rectangle_outline(settings.WIDTH//2, settings.HEIGHT//2 + 150, 500, 120, arcade.color.BLACK, border_width=3)
        arcade.draw_rectangle_outline(settings.WIDTH//2, settings.HEIGHT//2 + 30, 500, 120, arcade.color.BLACK, border_width=3)
        arcade.draw_rectangle_outline(settings.WIDTH//2, settings.HEIGHT//2 - 90, 500, 120, arcade.color.BLACK, border_width=3)

        arcade.draw_rectangle_outline(settings.WIDTH//2 - 200, self.indicator_y, 86, 20, arcade.color.GOLD, border_width=2)

        arcade.draw_rectangle_filled(settings.WIDTH//2, 60, settings.WIDTH, 120, arcade.color.WHITE)
        arcade.draw_rectangle_outline(settings.WIDTH//2, 60, settings.WIDTH - 3, 120, arcade.color.BLACK, 3)
        arcade.draw_text("Use arrow keys to choose file slot...", 40, 100, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")
        arcade.draw_text("Press the enter key to select...", 40, 60, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.selection > 0:
            self.indicator_y += 120
            self.selection -= 1

        if key == arcade.key.DOWN and self.selection < 2:
            self.indicator_y -= 120
            self.selection += 1

        if key == arcade.key.ENTER:
            if self.saves[self.selection] is None:
                # arcade.draw_text(f"Create new save file?", 40, 100, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")
                self.director.next_view()
            else:
                # arcade.draw_text(f"Load {self.saves[self.selection]}?", 40, 100, arcade.color.BLACK, 14, anchor_x="left", anchor_y="top")
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
