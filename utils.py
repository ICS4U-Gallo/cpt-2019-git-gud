from typing import List, Dict
import random as r
import arcade
import settings


class FakeDirector:
    """A class to fake the presence of a Director when running
    a view directly.
    """

    def __init__(self, close_on_next_view=True):
        """Create a new FakeDirector object.

        Args:
            exit_on_complete: Whether to close the program when
                a view being run directly calls:
                self.director.next_view()
        """
        self._exit_on_complete = close_on_next_view

    def next_view(self) -> None:
        print("SCENE COMPLETE.")
        if self._exit_on_complete:
            exit()

    def specific_view(self, view) -> None:
        print("SCENE COMPLETE.")
        if self._exit_on_complete:
            exit()


class Attack:
    attacks = []

    def __init__(self, attack: str, attack_power: int,
                 attack_type: str, attack_audio: str = None):
        self._attack = attack.lower()
        self._attack_power = attack_power
        self._attack_type = attack_type.lower()
        self._attack_audio = attack_audio
        Attack.attacks.append(self)

    def set_attack(self, attack: str) -> None:
        self._attack = attack.lower()

    def get_attack(self) -> int:
        return self._attack

    def set_attack_power(self, attack_power: int) -> None:
        self._attack_power = attack_power

    def get_attack_power(self) -> int:
        return self._attack_power

    def set_attack_type(self, type: str) -> None:
        self._attack_type = type.lower()

    def get_attack_type(self) -> str:
        return self._attack_type

    def set_attack_audio(self, audio: str) -> None:
        self._attack_audio = audio

    def get_attack_audio(self) -> str:
        return self._attack_audio


class Pokemon:
    def __init__(self, name: str, health_points: int, Type: str, passive_ability: str, image: str, sound: str, level: int,
                 attack:str=None, attack_power:int=None, attack_type:str=None, attack_audio:str=None,
                 moveset2:Dict[str,dict]=None, experience_points: int = 0, item: str = None):
        if attack != None and attack_power != None and attack_type != None:
            super().__init__(attack, attack_power, attack_type, attack_audio)
        self._name = name
        self._max_hp = health_points
        self._current_hp = health_points
        self._type = Type.lower()
        self._passive = passive_ability
        self._debuff = None
        self._image = image
        self._lvl = level
        self._moveset2 = moveset2
        self._exp = experience_points
        self._item = item

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name.lower()

    def get_max_hp(self) -> int:
        return self._max_hp

    def set_max_hp(self, hp: int) -> None:
        self._hp = hp

    def get_current_hp(self) -> int:
        return self._current_hp

    def set_current_hp(self, hp: int) -> None:
        self._hp = hp

    def get_type(self) -> str:
        return self._type

    def set_type(self, type: str) -> None:
        self._type = type.lower()

    def get_passive(self) -> str:
        return self._passive

    def set_passive(self, passive: str) -> None:
        self._passive = passive.lower()

    def get_debuff(self) -> str:
        return self._debuff

    def get_moveset(self, attack: int) -> Attack:
        return Attack.attacks[attack]

    def add_attack(self, attack: str, power: int,
                   type: str, audio:str=None) -> None:
        if len(Attack.attacks) <= 4:
            super().__init__()
        else:
            raise ValueError("Maximum attacks reached. Max: 4")

    def get_pokemon_pic(self) -> str:
        return self._pokemon_pic

    def set_pokemon_pic(self, file: str) -> None:
        self._pokemon_pic = file

    def get_pokemon_sound(self) -> str:
        return self._pokemon_sound

    def set_pokemon_sound(self, audio: str) -> None:
        self._pokemon_sound = audio

    def get_lvl(self) -> int:
        return self._lvl

    def set_lvl(self, lvl: int) -> None:
        self._lvl = lvl

    def get_exp(self) -> int:
        return self._exp

    def set_exp(self, points: int) -> None:
        self._exp = points

    def get_item(self) -> str:
        return self._item

    def set_item(self, item: str) -> None:
        self._item = item.capitalize()


class AttackSprite(arcade.Sprite):
    """
    Attrs:
        pokemon_sprite = a PokemonSprite object that gives information on the sprite movement direction
        attack_info = a dictionary of the attack move, relaying information on it's name, damage, speed and sprite info (type, scale)
        attack_tier = a string of the type of attack that is being used (normal, special)
            - normal attacks refer to attacks with lower cooldowns and lower damage ranges
            - special attacks refer to attacks with higher cooldowns, higer damage ranges, and other effects such as stuns and damage over time
        boundary = a dictionary of the different side boundaries of the sprite, deleting itself when it passes these boundaries
    """
    all_attacks = arcade.SpriteList()

    def __init__(self, pokemon_sprite: object, attack_info: Dict, attack_tier: str, boundary: Dict[str, int]):
        super().__init__()
        self.direction = pokemon_sprite._character_direction
        self.ally = pokemon_sprite._entity_type
        if self.ally == "enemy":
            self._set_alpha(100)
        self.tier = attack_tier
        self.name = attack_info["Name"].lower()
        self.damage = attack_info["Damage"]
        self.sprite_type = attack_info["Sprite Type"][0]
        self.speed = attack_info["Speed"]
        self.scale = attack_info["Scale"]
        self.damaging = True
        self.collided = False
        self._set_alpha(180)
        if len(attack_info["Sprite Type"]) > 1:
            self.reflection = attack_info["Sprite Type"][1]
            self.animate = False
        self.texture = arcade.load_texture(
            f"images/attacks/{self.name}.png", scale=self.scale)
        if self.sprite_type == "Projectile":
            if self.direction == "up":
                self.set_position(pokemon_sprite.center_x,
                                  pokemon_sprite.top-10)
            elif self.direction == "down":
                self.set_position(pokemon_sprite.center_x,
                                  pokemon_sprite.bottom+10)
            elif self.direction == "left":
                self.set_position(pokemon_sprite.left+10,
                                  pokemon_sprite.center_y-10)
            elif self.direction == "right":
                self.set_position(pokemon_sprite.right-10,
                                  pokemon_sprite.center_y-10)
            self.boundary_top = boundary["top"]
            self.boundary_bottom = boundary["bottom"]
            self.boundary_left = boundary["left"]
            self.boundary_right = boundary["right"]
        elif self.sprite_type == "Stationary":
            if self.direction == "up":
                self.set_position(pokemon_sprite.center_x,
                                  pokemon_sprite.top+self.height//2)
            elif self.direction == "down":
                self.set_position(pokemon_sprite.center_x,
                                  pokemon_sprite.bottom+self.height//2)
            elif self.direction == "left":
                self.set_position(pokemon_sprite.left-self.width //
                                  2, pokemon_sprite.bottom+self.height//2)
            elif self.direction == "right":
                self.set_position(pokemon_sprite.right+self.width //
                                  2, pokemon_sprite.bottom+self.height//2)
            self.timer = 100
        AttackSprite.all_attacks.append(self)

    @classmethod
    def remove_all(cls):
        """
        Removes sprites from all sprite lists assosiated with them
        """
        for sprite in cls.all_attacks:
            sprite.remove_from_sprite_lists()

    def update(self):
        if self.sprite_type == "Projectile":
            if self.collided:
                self.remove_from_sprite_lists()
            if self.direction == "up":
                self.center_y += self.speed
                if self.bottom >= self.boundary_top:
                    self.remove_from_sprite_lists()
            elif self.direction == "down":
                self.center_y -= self.speed
                if self.top <= self.boundary_bottom:
                    self.remove_from_sprite_lists()
            elif self.direction == "left":
                self.center_x -= self.speed
                if self.right <= self.boundary_left:
                    self.remove_from_sprite_lists()
            elif self.direction == "right":
                self.center_x += self.speed
                if self.left >= self.boundary_right:
                    self.remove_from_sprite_lists()
        elif self.sprite_type == "Stationary":
            if self.timer == 0:
                self.remove_from_sprite_lists()
            self.timer -= 1

    def update_animation(self, delta_time=1 / 60):
        if hasattr(self, "animate"):
            if self.timer % 20 == 0:
                if self.animate:
                    self.animate = False
                    self.damaging = False
                else:
                    self.animate = True
                    self.damaging = True
            if self.reflection == "Mirrored":
                self.texture = arcade.load_texture(
                    f"images/attacks/{self.name}.png", scale=self.scale, mirrored=self.animate)
            elif self.reflection == "Flipped":
                self.texture = arcade.load_texture(
                    f"images/attacks/{self.name}.png", scale=self.scale, flipped=self.animate)


class PokemonSprite(arcade.Sprite):
    player = None
    current_enemy = None
    all_enemies = arcade.SpriteList()
    all_entities = arcade.SpriteList()
    stronger_enemies = []

    def __init__(self, entity_type: str, pokemon: object, location: tuple, speed: int, direction: str = "down", detection_range: int = 50, pathing: str = "stationary"):
        super().__init__()
        self.pokemon = pokemon
        self._detection_range = detection_range
        self._entity_type = entity_type
        self.set_position(location[0], location[1])
        self._character_direction = direction
        self._movement = {"up": False, "down": False,
                          "left": False, "right": False}
        self._moving = True
        self._speed = speed
        self.stunned = False
        self.stun_timer = 0
        self.stun_duration = 80
        self.ability1 = self.pokemon._moveset2["Normal"]
        if self._entity_type == "player":
            self.score = 0
            self.ability1["Active"] = False
            self._moving = True
            self.ability2 = self.pokemon._moveset2["Special"]
            self.ability2["Active"] = False
            PokemonSprite.player = self
        elif self._entity_type == "enemy":
            self.ability1["Active"] = True
            self.pathing = pathing
            PokemonSprite.all_enemies.append(self)
        PokemonSprite.all_entities.append(self)

        self._main_path = f"images/pokemon/{pokemon.get_name()}"
        self._animation_timer = 0
        self._walk_texture_num = 0

        self.idle_textures = {"up": None, "down": None,
                              "left": None, "right": None}
        for key in self.idle_textures:
            texture = arcade.load_texture(
                f"{self._main_path}/idle-{key}.png", scale=1.5)
            self.idle_textures[key] = texture

        self.walk_textures = {"up": [], "down": [],
                              "left": [], "right": []}
        for key in self.walk_textures.keys():
            texture1 = arcade.load_texture(
                f"{self._main_path}/walk-{key}0.png", scale=1.5)
            if key == "left" or key == "right":
                texture2 = arcade.load_texture(
                    f"{self._main_path}/idle-{key}.png", scale=1.5)
            else:
                texture2 = arcade.load_texture(
                    f"{self._main_path}/walk-{key}1.png", scale=1.5)
            self.walk_textures[key].append(texture1)
            self.walk_textures[key].append(texture2)

        self.texture = self.idle_textures[self._character_direction]
        self.set_boundaries()

    def get_speed(self) -> int:
        return self._speed

    def set_speed(self, value: int):
        self._speed = value

    def get_movement(self) -> Dict[str, bool]:
        return self._movement

    def set_movement(self, direction: str, moving: bool) -> None:
        self._movement[direction] = moving

    def get_character_direction(self) -> str:
        """Returns the direction the sprite is facing 
        """
        return self._character_direction

    @staticmethod
    def boundary(top: int = "default", bottom: int = 0, left: int = 0, right: int = "default") -> Dict[str, int]:
        """Returns a dictionary of boundaries
        """
        if top == "default":
            top = settings.HEIGHT
        if right == "default":
            right = settings.WIDTH
        return {"top": top, "bottom": bottom, "left": left, "right": right}

    def set_boundaries(self) -> None:
        """Set sprite boundaries
        """
        boundary = PokemonSprite.boundary()
        self.boundary_top = boundary["top"]
        self.boundary_bottom = boundary["bottom"]
        self.boundary_left = boundary["left"]
        self.boundary_right = boundary["right"]

    @classmethod
    def remove_all_enemies(cls) -> None:
        """Remove all sprites from sprite lists they are associated with
        """
        for enemy in cls.all_enemies:
            enemy.remove_from_sprite_lists()
        cls.stronger_enemies = []

    @classmethod
    def detect_stronger_enemies(cls, enemies: List[object] = None) -> List[object]:
        """Returns a list of sprites that are levels 2 or more than the player
        Args:
            enemies = a list of PokemonSprite enemies
        """
        if enemies is None:
            enemies = cls.all_enemies
        if len(enemies) == 0:
            return []
        elif enemies[0].pokemon.get_lvl() >= PokemonSprite.player.pokemon.get_lvl() + 2:
            enemies[0].stun_duration = 120
            return [enemies[0]] + cls.detect_stronger_enemies(enemies[1:])
        return cls.detect_stronger_enemies(enemies[1:])

    def execute(self, rangeA: int, rangeB: int) -> None:
        """Chance to kill a sprite
        Args:
            rangeA = numerator
            rangeB = denominator
            change percentage = (rangeA/rangeB * 100) percent
        """
        list_of_lvls = []
        for enemy in PokemonSprite.all_enemies:
            if enemy.pokemon._lvl not in list_of_lvls and enemy not in PokemonSprite.stronger_enemies and enemy.pokemon._lvl < PokemonSprite.player.pokemon._lvl:
                list_of_lvls.append(enemy.pokemon._lvl)
        lvl_list = bubble_sort(list_of_lvls)

        if binary_search(self.pokemon._lvl, lvl_list) <= len(lvl_list)-1:
            if r.randint(rangeA, rangeB) == 1:
                self.pokemon._current_hp -= self.pokemon._current_hp

    def attack1(self) -> None:
        """First ability (normal), creates AttackSprite
        """
        if self.ability1["Active"] and self.ability1["Cooldown"][0] == self.ability1["Cooldown"][1]:
            AttackSprite(self, self.ability1, "normal",
                         PokemonSprite.boundary())
            self.ability1["Cooldown"][0] = 0

    def attack2(self) -> None:
        """Second ability (special), creates AttackSprite
        """
        if hasattr(self, "ability2"):
            if self.ability2["Active"] and self.ability2["Cooldown"][0] == self.ability2["Cooldown"][1]:
                AttackSprite(self, self.ability2, "special",
                             PokemonSprite.boundary())
                self.ability2["Cooldown"][0] = 0

    @classmethod
    def follow(cls):
        """Sets enemy botting to follow player if none are active
        """
        if len(cls.all_enemies) > 0:
            for sprite in cls.all_enemies:
                if sprite.pathing == "follow":
                    return True
            cls.all_enemies[0].pathing = "follow"
            cls.all_enemies[0].ability1["Active"] = False
            cls.current_enemy = cls.all_enemies[0]
            return True
        cls.current_enemy = None
        return None

    def damaged(self):
        """Decreases health to pokemons if they are hit by attacks, including status ailments such as stuns
        """
        stronger = False
        if self in PokemonSprite.all_enemies:
            stronger = True
        for attack in self.collides_with_list(AttackSprite.all_attacks):
            if attack.ally != self._entity_type:
                if self._entity_type == "player" and attack.damaging:
                    self.pokemon._current_hp -= attack.damage
                if self._entity_type == "enemy":
                    if self.pathing == "follow" and attack.damaging:
                        self.pokemon._current_hp -= attack.damage
                    if attack.tier == "special":
                        self.stunned = True
                        self.stun_timer = 0
                    else:
                        if self.pathing == "follow":
                            self.execute(1, 20)
                attack.collided = True

    def update(self):
        if self.pokemon.get_current_hp() <= 0:
            if self._entity_type == "enemy":
                PokemonSprite.player.pokemon._current_hp += 100
                if PokemonSprite.player.pokemon._current_hp > PokemonSprite.player.pokemon._max_hp:
                    PokemonSprite.player.pokemon._current_hp = PokemonSprite.player.pokemon._max_hp
                PokemonSprite.player.score += 10 * self.pokemon._lvl
            self.remove_from_sprite_lists()

        if len(self.collides_with_list(AttackSprite.all_attacks)) > 0:
            self.damaged()

        if not self.stunned:
            if self._alpha != 255:
                self._set_alpha(255)

            if self.ability1["Active"]:
                self.attack1()
            if self.ability1["Cooldown"][0] < self.ability1["Cooldown"][1]:
                self.ability1["Cooldown"][0] += 1
            if self._entity_type == "player":
                if self.ability2["Active"]:
                    self.attack2()
                if self.ability2["Cooldown"][0] < self.ability2["Cooldown"][1]:
                    self.ability2["Cooldown"][0] += 1
                collision_list = self.collides_with_list(
                    PokemonSprite.all_enemies)

            if self._entity_type == "enemy":
                collision_list = self.collides_with_list(
                    PokemonSprite.all_entities)
                if self.pathing == "follow":
                    if self.center_y - PokemonSprite.player.center_y > 0:
                        if self.bottom - PokemonSprite.player.top > 0:
                            self._movement["down"] = True
                            self._movement["up"] = False
                    else:
                        if self.top - PokemonSprite.player.bottom < 0:
                            self._movement["up"] = True
                            self._movement["down"] = False

                    if self.center_x - PokemonSprite.player.center_x > 0:
                        if self.left - PokemonSprite.player.right > 0:
                            self._movement["left"] = True
                            self._movement["right"] = False
                    else:
                        if self.right - PokemonSprite.player.left < 0:
                            self._movement["right"] = True
                            self._movement["left"] = False

            if self._movement["up"] and self.top < self.boundary_top:
                if len(collision_list) > 0:
                    self.change_y = -self._speed
                    self._movement["up"] = False
                else:
                    self.change_y = self._speed
            elif self._movement["down"] and self.bottom > self.boundary_bottom:
                if len(collision_list) > 0:
                    self.change_y = self._speed
                    self._movement["down"] = False
                else:
                    self.change_y = -self._speed
            else:
                self.change_y = 0

            if self._movement["left"] and self.left > self.boundary_left:
                if len(collision_list) > 0:
                    self.change_x = self._speed
                    self._movement["left"] = False
                else:
                    self.change_x = -self._speed
            elif self._movement["right"] and self.right < self.boundary_right:
                if len(collision_list) > 0:
                    self.change_x = -self._speed
                    self._movement["right"] = False
                else:
                    self.change_x = self._speed
            else:
                self.change_x = 0

            self._set_collision_radius(16)
            self.position = [self._position[0] +
                             self.change_x, self._position[1] + self.change_y]
        else:
            if self.stun_timer == self.stun_duration:
                self.stun_timer = 0
                self.stunned = False
            self.stun_timer += 1
            self._set_alpha(180)

    def update_animation(self, delta_time: float = 1/60):
        if self.change_x == 0 and self.change_y == 0:
            if self._character_direction == "left" or self._character_direction == "right":
                if self._walk_texture_num != 0:
                    self.texture = self.walk_textures[self._character_direction][0]
            self.texture = self.idle_textures[self._character_direction]
            self._walk_texture_num = 0
            self._animation_timer = 0
        elif self._animation_timer == 0:
            if self._walk_texture_num == 0:
                self._walk_texture_num = 1
            else:
                self._walk_texture_num = 0
        else:
            self._animation_timer += 1

        if self._movement["left"]:
            self._character_direction = "left"
            self.texture = self.walk_textures["left"][self._walk_texture_num]
            self._animation_timer += 1
        elif self._movement["right"]:
            self._character_direction = "right"
            self.texture = self.walk_textures["right"][self._walk_texture_num]
            self._animation_timer += 1
        elif self._movement["down"]:
            self._character_direction = "down"
            self.texture = self.walk_textures["down"][self._walk_texture_num]
            self._animation_timer += 1
        elif self._movement["up"]:
            self._character_direction = "up"
            self.texture = self.walk_textures["up"][self._walk_texture_num]
            self._animation_timer += 1

        if self._animation_timer > 7 * 3 - (self._speed * 3):
            self._animation_timer = 0


class Trainer:
    def __init__(self, name: str, pokemons: List[Pokemon],
                 items: Dict[str, int] = None, money: int = None):
        self._name = name.lower()
        self._pokemons = pokemons
        self._items = items

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name.lower()

    def get_items(self) -> Dict[str, int]:
        return self._items

    def remove_item(self, item: str, amount: int) -> None:
        self._items[item.capitalize()] -= amount

    def get_pokemons(self) -> List[Pokemon]:
        return self._pokemons


class Player(Trainer):
    def __init__(self, name, pokemons, items=None, money=None):
        super().__init__(name, pokemons, items=items, money=money)
        self._money = money

    def add_item(self, item: str, amount: int) -> None:
        self._items[item.capitalize()] += amount

    def get_money(self) -> int:
        return self._money

    def set_money(self, money: int) -> None:
        self._money = money

    def add_money(self, amount: int) -> None:
        self._money += amount

    def subtract_money(self, amount: int) -> None:
        self._money -= amount

    def add_pokemon(self, pokemon: Pokemon) -> None:
        if len(self._pokemons) <= 6:
            self._pokemons.append(pokemon)
        else:
            return ValueError("Too many pokemon. Max: 6")  # place in pc

    def release_pokemon(self, name: str) -> None:
        if len(self._pokemons) == 1:
            return ValueError("Cannot remove last pokemon. Min: 1")
        else:
            for i in range(self._pokemons):
                if self._pokemons[i].get_name == name.lower():
                    del self._pokemons[i]


# # class PC():
#     def __init__(self):
#         self._stored = {}
#         self._pages = []

#         for page in range(20):
#             for i in range(100):
#                 self._stored[i] = None
#             self._pages[page] = self._stored

#     def add_pokemon(self, page_number: int, place_number: int, pokemon: Pokemon):
#         for empty in self._stored[page_number]:
#             pass


class CPU(Trainer):  # IN PROGRESS
    def __init__(self, name:  str, pokemons: List[Pokemon],
                 items: Dict[str, int] = None):
        super().__init__(name, pokemons, items)

    def normal(self, special: bool):
        if special:
            pass


class Battle():  # IN PROGRESS
    turns = 0

    def __init__(self, player: Player, cpu: CPU = None, wild_pokemon: Pokemon = None):
        self._player = player
        self._cpu = cpu
        self._wild_pokemon = wild_pokemon
        self._moveset = player._pokemons[0].get_moveset

    def attack(self, pokemon: object, ability, opponent: object) -> None:
        # moveset = {"ability name": {"type": str, "power_points": int, "damage": int, "debuffs: str/None"}}
        if self._moveset[ability]["power_points"] == 0:
            return "Unable to use ability"
        elif self._moveset[ability]["type"] in settings.strengths[opponent._type]:
            opponent._hp -= 1.5 * self._moveset[ability]["damage"]
        elif self._moveset[ability]["type"] in settings.weaknesses[opponent.type]:
            opponent._hp -= 0.5 * self._moveset[ability]["damage"]
        else:
            opponent._hp -= self._moveset[ability]["damage"]

        # exp gain: a*t*b*L/(7*s)
        # a: a=1 if wild pokemon, a=1.5 if trainer owned
        # t: t=1 if pokemon is trainer caught, t = 1.5 if pokemon is obtained from trading
        # b: pokemon's based exp value
        # L: the level of the defeated pokemon
        # s: ...

    def catch(self, enemy_hp: int):  # APPEND TO PC IF CAUGHT AND POKESLOTS ARE FULL
        if self._wild_pokemon is not None:
            if enemy_hp == self._wild_pokemon._hp:
                if r.randint(1, 100) <= 20:
                    return True
                return False
            elif enemy_hp <= self._wild_pokemon._hp * 0.7:
                if r.randint(1, 100) <= 40:
                    return True
                return False
            elif enemy_hp <= self._wild_pokemon._hp * 0.5:
                if r.randint(1, 100) <= 50:
                    return True
                return False
            elif enemy_hp <= self._wild_pokemon._hp * 0.3:
                if r.randint(1, 100) <= 70:
                    return True
                return False
            elif enemy_hp <= self._wild_pokemon._hp * 0.1:
                if r.randint(1, 100) <= 90:
                    return True
                return False
            else:
                return True


def bubble_sort(array: List[int]) -> List[int]:
    while True:
        changed = False
        for i in range(len(array)):
            if i != len(array) - 1:
                proceeding = array[i+1]
                if array[i] > proceeding:
                    array[i+1] = array[i]
                    array[i] = proceeding
                    changed = True
        if not changed:
            return array


def merge_sort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array

    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])

    new_array = []
    left_marker = 0
    right_marker = 0

    while left_marker < len(left) and right_marker < len(right):
        if left[left_marker] <= right[right_marker]:
            new_array.append(left[left_marker])
            left_marker += 1
        else:
            new_array.append(right[right_marker])
            right_marker += 1

    while left_marker < len(left):
        new_array.append(left[left_marker])
        left_marker += 1

    while right_marker < len(right):
        new_array.append(right[right_marker])
        right_marker += 1

    return new_array


def linear_search(target: int, data: List) -> int:
    for i, num in enumerate(data):
        if num == target:
            return i

    return -1


def binary_search(target: int, numbers: List) -> int:
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == numbers[mid]:
            return mid
        elif target > numbers[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1
