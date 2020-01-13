import arcade

import settings
import utils

class Chapter3View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BABY_BLUE)
        self.background = settings.BATTLE_BACKGROUND
        

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(settings.WIDTH // 2, settings.HEIGHT // 2 + 150,
                                      settings.WIDTH, settings.HEIGHT // 2, self.background)
        
        arcade.draw_rectangle_outline(settings.WIDTH // 2, settings.HEIGHT // 20, settings.WIDTH // 5, settings.HEIGHT // 20, arcade.color.BLACK)

    def on_key_press(self, key, modifiers):
        pass

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
    my_view = Chapter3View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
