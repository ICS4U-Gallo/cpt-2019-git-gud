import arcade

import random

import settings

import utils


class Part1(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ASH_GREY)
        if not settings.shown:
            for i in range(7):
                enemy = utils.Pokemon("Rattata", 200, "normal", "", "", "", random.randint(8, 15),
                                      moveset2={"Normal": {"Name": "Electro Ball", "Damage": 4, "Cooldown": [160, 160],
                                                           "Sprite Type": ["Projectile"], "Speed": 4, "Scale": 0.4}})
                sprite = utils.PokemonSprite(
                    "enemy", enemy, (settings.WIDTH, 40 + i * 90), 2, "left")

            for i in range(7):
                enemy = utils.Pokemon("Rattata", 200, "normal", "", "", "", random.randint(8, 15),
                                      moveset2={"Normal": {"Name": "Electro Ball", "Damage": 4, "Cooldown": [160, 160],
                                                           "Sprite Type": ["Projectile"], "Speed": 4, "Scale": 0.4}})
                sprite = utils.PokemonSprite(
                    "enemy", enemy, (10, 40 + i * 90), 2, "right")

            if utils.PokemonSprite.player is None:
                self.pokemon = utils.Pokemon("Pikachu", 400, "electric", "", "", "", 10,
                                             moveset2={"Normal": {"Name": "Electro Ball", "Damage": 6, "Cooldown": [30, 30],
                                                                  "Sprite Type": ["Projectile"], "Speed": 8, "Scale": 0.4},
                                                       "Special": {"Name": "ThunderBolt", "Damage": 1, "Cooldown": [240, 240],
                                                                   "Sprite Type": ["Stationary", "Mirrored"], "Speed": 4, "Scale": 1}})
                utils.PokemonSprite("player", self.pokemon,
                                    (settings.WIDTH//2, settings.HEIGHT//2), 2)
            utils.PokemonSprite.stronger_enemies = utils.PokemonSprite.detect_stronger_enemies()
            self.display_rect = arcade.Sprite(
                center_x=settings.WIDTH//2, center_y=settings.HEIGHT//2)
            self.display_rect.texture = arcade.make_soft_square_texture(
                360, arcade.color.BLACK, center_alpha=150, outer_alpha=150)

            settings.shown = True

    def on_draw(self):
        arcade.start_render()
        self.display_rect.draw()
        arcade.draw_text(f"HEALTH: {utils.PokemonSprite.player.pokemon.get_current_hp()}", settings.WIDTH//2,
                         settings.HEIGHT//2+100, arcade.color.WHITE, 18, anchor_x="center", anchor_y="center")
        arcade.draw_text(f"SCORE: {utils.PokemonSprite.player.score}", settings.WIDTH//2, settings.HEIGHT//2-100,
                         arcade.color.WHITE, 18, anchor_x="center", anchor_y="center")
        utils.PokemonSprite.player.draw()
        utils.PokemonSprite.all_enemies.draw()
        utils.AttackSprite.all_attacks.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            utils.PokemonSprite.player.set_movement("up", True)
        elif key == arcade.key.DOWN:
            utils.PokemonSprite.player.set_movement("down", True)
        if key == arcade.key.LEFT:
            utils.PokemonSprite.player.set_movement("left", True)
        elif key == arcade.key.RIGHT:
            utils.PokemonSprite.player.set_movement("right", True)

        if key == arcade.key.A:
            utils.PokemonSprite.player.ability1["Active"] = True
        if key == arcade.key.S:
            utils.PokemonSprite.player.ability2["Active"] = True

    def on_key_release(self, key, _modifiers):
        if key == arcade.key.UP:
            utils.PokemonSprite.player.set_movement("up", False)
        elif key == arcade.key.DOWN:
            utils.PokemonSprite.player.set_movement("down", False)
        if key == arcade.key.LEFT:
            utils.PokemonSprite.player.set_movement("left", False)
        elif key == arcade.key.RIGHT:
            utils.PokemonSprite.player.set_movement("right", False)

        if key == arcade.key.A:
            utils.PokemonSprite.player.ability1["Active"] = False
        if key == arcade.key.S:
            utils.PokemonSprite.player.ability2["Active"] = False

    def on_update(self, delta_time):
        utils.PokemonSprite.player.update()
        utils.PokemonSprite.player.update_animation()
        utils.PokemonSprite.all_enemies.update()
        utils.PokemonSprite.all_enemies.update_animation()
        utils.AttackSprite.all_attacks.update()
        utils.AttackSprite.all_attacks.update_animation()
        if utils.PokemonSprite.follow() is None:
            utils.AttackSprite.remove_all()
            utils.PokemonSprite.remove_all_enemies()
            settings.shown = False
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
    my_view = Part1()
    my_view.director = FakeDirector(close_on_next_view=False)
    window.show_view(my_view)
    arcade.run()
