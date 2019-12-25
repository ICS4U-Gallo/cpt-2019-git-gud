import arcade

import settings

# AM WORKING ON IT PLS DW ILL FIX THE SELECTION AND MAKE IT WORKABLE SOON I PROMISE
# - JOSH


class Chapter2View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.example_rects = [0,   1,   2 ,  3,   4,   5,
                                           6,   7,   8,   9,   10, 11,
                                           12, 13, 14, 15, 16, 17,
                                           18, 19, 20, 21, 22, 23,
                                           24, 25, 26, 27, 28, 29]
        self.selected_rect_x = 0
        self.selected_rect_y = 0
        self.pos_rect_x = 0
        self.pos_rect_y = 0
        

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
        
        arcade.draw_rectangle_outline(settings.WIDTH - 703 + self.selected_rect_x * (settings.WIDTH // 1.1) // 6,
                                      settings.HEIGHT - 122 - self.selected_rect_y * (settings.HEIGHT // 2.2) // 4,
                                      (settings.WIDTH // 1.1) // 6, (settings.HEIGHT // 2.2) // 4,
                                      arcade.color.GOLD, 5)
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            if self.selected_rect_x % 6 == 5:
                self.pos_rect_x -= 5
                self.selected_rect_x -= 5
                print(self.selected_rect_x)
            else:
                self.pos_rect_x += 1
                self.selected_rect_x += 1
                print(self.selected_rect_x)
        
        if key == arcade.key.LEFT:
            if self.selected_rect_x % 6 == 0:
                self.pos_rect_x += 5
                self.selected_rect_x += 5
                print(self.selected_rect_x)
            else:
                self.pos_rect_x -= 1
                self.selected_rect_x -= 1
                print(self.selected_rect_x)
        
        if key == arcade.key.UP:
            if self.pos_rect_y % 6 <= 5 and self.pos_rect_x <= 5:
                self.selected_rect_y += 6
                self.pos_rect_y += 24
                self.pos_rect_x += 24
                print(self.selected_rect_y)
            else:
                self.pos_rect_y -= 6
                self.selected_rect_y -= 1
                self.pos_rect_x -=6
                print(self.selected_rect_y)
        
        if key == arcade.key.DOWN:
            if self.pos_rect_y % 6 <= 5 and self.pos_rect_x >= 24:
                self.selected_rect_y -= 6
                self.pos_rect_y -= 24
                self.pos_rect_x -= 24
                print(self.selected_rect_y)
            else:
                self.pos_rect_y += 6
                self.selected_rect_y += 1
                self.pos_rect_x += 6
                print(self.selected_rect_y)
                
                
                
                

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
