import arcade

import settings


class Chapter1View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.chosen = False
        self.genders = [False, False, False]
        self.gender = 0
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Character Select", settings.WIDTH // 20, 
                         settings.HEIGHT - settings.WIDTH // 25, arcade.color.WHITE, 
                         30, 0, "left", 'Comic Sans', True, False, "left", "top")
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            if self.gender == 2:
                self.gender = 0
            else:
                self.gender += 1
        
        if key == arcade.key.LEFT:
            if self.gender == 0:
                self.gender = 2
            else:
                self.gender -= 1
        
        if self.chosen and key == arcade.key.ENTER:
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
