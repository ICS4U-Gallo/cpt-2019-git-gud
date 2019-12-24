import arcade

import settings


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(
            "images/screen_menu_background.png")
        self.switch = True
        self.count = 0
        self.music = arcade.load_sound("audio/screen_menu.mp3")
        self.music.play()

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_texture_rectangle(settings.WIDTH // 2, settings.HEIGHT // 2,
                                      settings.WIDTH, settings.HEIGHT, self.background)
        
        if self.switch:
            arcade.draw_text("ENTER ", settings.WIDTH // 2, settings.HEIGHT // 4,
                            arcade.color.GOLD, 30, 0,  "center", 'Comic Sans', True, False,
                            "center", "center")
            self.count += 1
            if self.count >= 50:
                self.switch = False
                self.count = 0
                
        elif not self.switch:
            arcade.draw_text("ENTER ", settings.WIDTH // 2, settings.HEIGHT // 4,
                            arcade.color.GOLDENROD, 30, 0,  "center", 'Comic Sans', True, False,
                            "center", "center")
            self.count += 1
            if self.count >= 50:
                self.switch = True
                self.count = 0
                
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
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
    my_view = MenuView()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
