import arcade

import settings
import utils

class Chapter3View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLUE_BELL)
        self.background = settings.BATTLE_BACKGROUND
        self.selected = 2
        self.btn_pokemon = False
        self.btn_fight = False
        self.btn_bag = False
        self.btn_fight_atk_1 = False
        self.btn_fight_atk_2 = False
        self.btn_fight_atk_3 = False
        self.btn_fight_atk_4 = False
        self.btn_pokemon_1 = False
        self.btn_pokemon_2 = False
        self.btn_pokemon_3 = False
        self.btn_pokemon_4 = False
        self.btn_pokemon_5 = False
        self.btn_pokemon_6 = False
        self.game_win = False
        self.game_lose = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(settings.WIDTH // 2, settings.HEIGHT // 2 + 150,
                                      settings.WIDTH, settings.HEIGHT // 2, self.background)
        
        arcade.draw_rectangle_filled(settings.WIDTH // 2 - 264, settings.HEIGHT //
                                     20 + 2, settings.WIDTH // 3, settings.HEIGHT // 10, arcade.color.GO_GREEN)
        arcade.draw_text("P O K E M O N", settings.WIDTH // 2 - 264,  settings.HEIGHT // 20 + 2,
                         arcade.color.WHITE, 25, 0, "center", 'Comic Sans', True, True, "center", "center", 0)

        if self.selected == 1:
            arcade.draw_rectangle_outline(settings.WIDTH // 2 - 264, settings.HEIGHT //
                                          20 + 2, settings.WIDTH // 3, settings.HEIGHT // 10, arcade.color.GOLD, 5)
        else:
            arcade.draw_rectangle_outline(settings.WIDTH // 2 - 264, settings.HEIGHT //
                                        20 + 2, settings.WIDTH // 3, settings.HEIGHT // 10, arcade.color.BLACK, 5)

        arcade.draw_rectangle_filled(settings.WIDTH // 2, settings.HEIGHT // 20 + 2,
                                     settings.WIDTH // 3 - 25, settings.HEIGHT // 10, arcade.color.RED_BROWN)
        arcade.draw_text("F I G H T", settings.WIDTH // 2, settings.HEIGHT // 20 + 2,
                         arcade.color.WHITE, 25, 0, "center", 'Comic Sans', True, True, "center", "center", 0)
        
        if self.selected == 2:
            arcade.draw_rectangle_outline(settings.WIDTH // 2, settings.HEIGHT // 20 + 2,
                                            settings.WIDTH // 3 - 25, settings.HEIGHT // 10, arcade.color.GOLD, 5)
        else:
            arcade.draw_rectangle_outline(settings.WIDTH // 2, settings.HEIGHT // 20 + 2,
                                            settings.WIDTH // 3 - 25, settings.HEIGHT // 10, arcade.color.BLACK, 5)

        arcade.draw_rectangle_filled(settings.WIDTH // 2 + 264, settings.HEIGHT // 20 + 2,
                                     settings.WIDTH // 3, settings.HEIGHT // 10, arcade.color.ORIOLES_ORANGE)
        arcade.draw_text("B A G", settings.WIDTH // 2 + 264, settings.HEIGHT // 20 + 2,
                         arcade.color.WHITE, 25, 0, "center", 'Comic Sans', True, True, "center", "center", 0)
        
        if self.selected == 3:
            arcade.draw_rectangle_outline(settings.WIDTH // 2 + 264, settings.HEIGHT //
                                            20 + 2, settings.WIDTH // 3, settings.HEIGHT // 10, arcade.color.GOLD, 5)
        else:
            arcade.draw_rectangle_outline(settings.WIDTH // 2 + 264, settings.HEIGHT //
                                            20 + 2, settings.WIDTH // 3, settings.HEIGHT // 10, arcade.color.BLACK, 5)

        if self.btn_fight:
            arcade.draw_rectangle_filled(settings.WIDTH // 2 - 130, settings.HEIGHT // 3 + 25,
                                        settings.WIDTH // 3, settings.HEIGHT // 10, arcade.color.DUTCH_WHITE)
            arcade.draw_text("A t t a c k  1", settings.WIDTH // 2 - 130, settings.HEIGHT // 3 + 25,
                            arcade.color.GRAY, 30, 0, "center", 'Comic Sans', True, True, "center", "center", 0)
            arcade.draw_rectangle_outline(settings.WIDTH // 2 - 130, settings.HEIGHT // 3 + 25,
                                        settings.WIDTH // 3, settings.HEIGHT // 10, arcade.color.BLACK, 5)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT and self.selected < 3:
            self.selected += 1
            print(self.selected)
        
        if key == arcade.key.LEFT and 1 < self.selected:
            self.selected -= 1
            print(self.selected)

        if key == arcade.key.ENTER and not self.btn_fight and not self.btn_bag and not self.btn_pokemon:
            if self.selected == 1:
                self.btn_pokemon = True
            elif self.selected == 2:
                self.btn_fight = True
                self.selected = 4
            elif self.selected == 3:
                self.btn_bag = True
        
        if self.btn_fight and not self.btn_bag and not self.btn_pokemon:
            if key == arcade.key.RIGHT and self.selected < 7:
                self.selected += 1
                print(self.selected)
            
            if key == arcade.key.LEFT and 4 < self.selected:
                self.selected -= 1
                print(self.selected)
            
            if key == arcade.key.ENTER:
                if self.selected == 4:
                    self.btn_fight_atk_1 = True
                elif self.selected == 5:
                    self.btn_fight_atk_2 = True
                elif self.selected == 6:
                    self.btn_fight_atk_3 = True
                elif self.selected == 7:
                    self.btn_fight_atk_4 = True
        
        if self.btn_pokemon and not self.btn_fight and not self.btn_pokemon:
            if key == arcade.key.RIGHT and self.selected < 13:
                self.selected += 1
                print(self.selected)

            if key == arcade.key.LEFT and self.selected > 8:
                self.selected -= 1
                print(self.selected)
            
            if key == arcade.key.ENTER:
                if self.selected == 8:
                    self.btn_pokemon_1 = True
                elif self.selected == 9:
                    self.btn_pokemon_2 = True
                elif self.selected == 10:
                    self.btn_pokemon_3 = True
                elif self.selected == 11:
                    self.btn_pokemon_4 = True
                elif self.selected == 12:
                    self.btn_pokemon_5 = True
                elif self.selected == 13:
                    self.btn_pokemon_6 = True            

        if self.game_win:
            self.director.next_view() # Move on
        elif self.game_lose:
            self.director.next_view() # Reset



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
