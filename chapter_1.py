import arcade

import settings

class Chapter1View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.chosen = False
        self.genders = [False, False, False]
        self.gender = 0
        self.ring_played_male = False
        self.ring_played_female = False
        self.ring_played_chosen  = False
        self.male = arcade.load_texture("images/char_male.png")
        self.female = arcade.load_texture("images/char_female.png")
        self.background_music = arcade.load_sound("audio/screen_menu.mp3")
        self.ring = arcade.load_sound("audio/menu_get.mp3")
        arcade.play_sound(self.background_music)
            
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Character Select", settings.WIDTH // 20, 
                         settings.HEIGHT - settings.WIDTH // 25, arcade.color.WHITE, 
                         30, 0, "left", 'Comic Sans', True, False, "left", "top")
        
        arcade.draw_texture_rectangle(settings.WIDTH // 5, settings.HEIGHT // 2,
                                      settings.WIDTH // 5, settings.HEIGHT // 2, self.male)
        arcade.draw_text("MALE", settings.WIDTH // 5, settings.HEIGHT // 5,
                         arcade.color.WHITE, 30, 0, "center", 'Comic Sans', True, True,
                         "center", "center")
        if self.gender == 0:
            arcade.draw_rectangle_outline(settings.WIDTH // 5, settings.HEIGHT // 2,
                                          settings.WIDTH // 5, settings.HEIGHT // 2,
                                          arcade.color.GOLD)
            if not self.ring_played_male:
                arcade.play_sound(self.ring)
                self.ring_played_male = True
        else:
            arcade.draw_rectangle_outline(settings.WIDTH // 5, settings.HEIGHT // 2,
                                          settings.WIDTH // 5, settings.HEIGHT // 2,
                                          arcade.color.AMAZON)
            self.ring_played_male = False
        
        arcade.draw_texture_rectangle(settings.WIDTH // 1.3, settings.HEIGHT // 2,
                                      settings.WIDTH // 5, settings.HEIGHT // 2, self.female)
        arcade.draw_text("FEMALE", settings.WIDTH // 1.25, settings.HEIGHT // 5,
                         arcade.color.WHITE, 30, 0, "center", 'Comic Sans', True, True,
                         "center", "center")
        if self.gender == 1:
            arcade.draw_rectangle_outline(settings.WIDTH // 1.3, settings.HEIGHT // 2,
                                          settings.WIDTH // 5, settings.HEIGHT // 2,
                                          arcade.color.GOLD)
            if not self.ring_played_female:
                arcade.play_sound(self.ring)
                self.ring_played_female = True
        else:
            arcade.draw_rectangle_outline(settings.WIDTH // 1.3, settings.HEIGHT // 2,
                                          settings.WIDTH // 5, settings.HEIGHT // 2,
                                          arcade.color.AMAZON)
            self.ring_played_female = False
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            if self.gender == 1:
                self.gender = 0
            else:
                self.gender += 1
        
        if key == arcade.key.LEFT:
            if self.gender == 0:
                self.gender = 1
            else:
                self.gender -= 1
        
        if not self.chosen and key == arcade.key.ENTER:
            self.chosen = True
        
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
