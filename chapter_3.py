import arcade

import settings
import utils

class Chapter3View(arcade.View):
    def on_show(self):
        pass
            
    def on_draw(self):
        arcade.start_render()

    def on_key_press(self, key, modifiers):
        pass
    

    if 
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
    my_view = Chapter1View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
