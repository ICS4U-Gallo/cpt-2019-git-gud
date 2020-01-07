import arcade

import settings


class Chapter2View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.selected_rect_x = 0
        self.selected_rect_y = 0
        self.pos_rect_x = 0
        self.pos_rect_y = 0
        self.characters = "abcdefghijklmnopqrstuvwxyz"
        self.character_location = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("What's your name?", settings.WIDTH // 20,
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
        x_count = 0
        y_count = 0                      
        for i in range(26):
            if i != 0:
                if i % 6 == 0 and i != 0:
                    y_count += 1
                    x_count = 0
                else:
                    x_count += 1
            arcade.draw_text(self.characters[i], settings.WIDTH - 703 + x_count * 121.3, settings.HEIGHT - 122 - y_count * 68.6, arcade.color.BLACK, 14, align="center")

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

        if self.selected_rect_x == 30 and key == arcade.key.ENTER:
            self.director.next_view()


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
