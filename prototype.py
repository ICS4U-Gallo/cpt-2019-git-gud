import arcade

import settings

import utils


class MINIGAME(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ASH_GREY)
        if not settings.shown:
            self.enemy = utils.Pokemon("Rattata", 200, "normal", "", "", "", 12,
                                         moveset2={"Normal": {"Name": "Electro Ball", "Damage": 0.6, "Cooldown": [40, 40],
                                                              "Sprite Type": ["Projectile"], "Speed": 8, "Scale": 0.4}})
            self.player = utils.PokemonSprite("enemy", self.enemy, (200, 100), 2)
            self.pokemon = utils.Pokemon("Pikachu", 100, "electric", "", "", "", 10,
                                         moveset2={"Normal": {"Name": "Electro Ball", "Damage": 5, "Cooldown": [40, 40],
                                                              "Sprite Type": ["Projectile"], "Speed": 8, "Scale": 0.4},
                                                   "Special": {"Name": "ThunderBolt", "Damage": 1, "Cooldown": [240, 240],
                                                               "Sprite Type": ["Stationary", "Mirrored"], "Speed": 4, "Scale": 1}})
            self.player = utils.PokemonSprite("player", self.pokemon, (100, 100), 2)
            self.player.set_boundaries()
            utils.PokemonSprite.stronger_enemies = utils.PokemonSprite.detect_stronger_enemies()
            settings.shown = True

    def on_draw(self):
        arcade.start_render()
        utils.PokemonSprite.player.draw()
        utils.PokemonSprite.all_enemies.draw()
        utils.AttackSprite.all_attacks.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.set_movement("up", True)
        elif key == arcade.key.DOWN:
            self.player.set_movement("down", True)
        if key == arcade.key.LEFT:
            self.player.set_movement("left", True)
        elif key == arcade.key.RIGHT:
            self.player.set_movement("right", True)
        
        if key == arcade.key.A:
            self.player.ability1["Active"] = True
        if key == arcade.key.S:
            self.player.ability2["Active"] = True

        if key == arcade.key.ENTER:
            self.director.next_view()

    def on_key_release(self, key, _modifiers):
        if key == arcade.key.UP:
            self.player.set_movement("up", False)
        elif key == arcade.key.DOWN:
            self.player.set_movement("down", False)
        if key == arcade.key.LEFT:
            self.player.set_movement("left", False)
        elif key == arcade.key.RIGHT:
            self.player.set_movement("right", False)
        
        if key == arcade.key.A:
            self.player.ability1["Active"] = False
        if key == arcade.key.S:
            self.player.ability2["Active"] = False

    def on_update(self, delta_time):
        utils.PokemonSprite.player.update()
        utils.PokemonSprite.player.update_animation()
        utils.PokemonSprite.all_enemies.update()
        utils.PokemonSprite.all_enemies.update_animation()
        utils.AttackSprite.all_attacks.update()
        utils.AttackSprite.all_attacks.update_animation()


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
