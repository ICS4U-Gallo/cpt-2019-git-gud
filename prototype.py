import arcade

import settings

import utils


class MINIGAME(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.player_list = arcade.SpriteList()
        self.player = utils.PokePlayer("Pikachu", "down", 2)
        self.player.center_x = settings.WIDTH//2
        self.player.center_y = settings.HEIGHT//2
        self.player_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.move("up")
        elif key == arcade.key.DOWN:
            self.player.move("down")
        if key == arcade.key.RIGHT:
            self.player.move("right")
        elif key == arcade.key.LEFT:
            self.player.move("left")

        if key == arcade.key.ENTER:
            self.director.next_view()

    def on_key_release(self, key, _modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

    def on_update(self, delta_time):
        self.player_list.update()
        self.player_list.update_animation()


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
    my_view = MINIGAME()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
