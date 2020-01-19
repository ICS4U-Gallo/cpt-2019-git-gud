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

    def set_attack(self, attack: str):
        self._attack = attack.lower()

    def get_attack(self):
        return self._attack

    def set_attack_power(self, attack_power: int):
        self._attack_power = attack_power

    def get_attack_power(self):
        return self._attack_power

    def set_attack_type(self, type: str):
        self._attack_type = type.lower()

    def get_attack_type(self):
        return self._attack_type

    def set_attack_audio(self, audio: str):
        self._attack_audio = audio

    def get_attack_audio(self):
        return self._attack_audio


class Pokemon(Attack):
    def __init__(self, name: str, health_points: int, Type: str, passive_ability: str, moveset: List[str],
                 image: str, sound: str, level: int, experience_points: int = 0, item: str = None):
        self._name = name
        self._hp = health_points
        self._type = Type.lower()
        self._passive = passive_ability
        self._debuff = None
        self._moveset = moveset
        self._image = image
        self._lvl = level
        self._exp = experience_points
        self._item = item

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name.lower()

    def get_hp(self):
        return self._hp

    def set_hp(self, hp: int):
        self._hp = hp

    def get_type(self):
        return self._type

    def set_type(self, type: str):
        self._type = type.lower()

    def get_passive(self):
        return self._passive

    def set_passive(self, passive: str):
        self._passive = passive.lower()

    def get_debuff(self):
        return self._debuff

    def get_moveset(self, attack: int):
        return Attack.attacks[attack]

    def add_attack(self, attack: str, power: int,
                   type: str, audio=None):
        if len(Attack.attacks) <= 4:
            super().__init__(attack, power, type, audio)
        else:
            raise ValueError("Maximum attacks reached. Max: 4")

    def get_pokemon_pic(self):
        return self._pokemon_pic

    def set_pokemon_pic(self, file: str):
        self._pokemon_pic = file

    def get_pokemon_sound(self):
        return self._pokemon_sound

    def set_pokemon_sound(self, audio: str):
        self._pokemon_sound = audio

    def get_lvl(self):
        return self._lvl

    def set_lvl(self, lvl: int):
        self._lvl = lvl

    def get_exp(self):
        return self._exp

    def set_exp(self, points: int):
        self.set_exp = points

    def get_item(self):
        return self._item

    def set_item(self, item: str):
        self._item = item.capitalize()


class Entity(arcade.Sprite):
    player = []
    enemy = []
    def __init__(self, entity_type: str, pokemon: object, location: tuple, speed:int=1, detection_range:int=50, direction:str="down"):
        super().__init__()
        self.pokemon = pokemon
        self._detection_range = detection_range
        self._entity_type = entity_type
        self.hidden = False
        if self._entity_type == "player":
            Entity.player.append(self)
        elif self._entity_type == "enemy":
            self.hidden = True
            Entity.enemy.append(self)
        self.set_position(location[0], location[1])
        self._character_direction = direction
        self._movement = {"up": False, "down": False,
                         "left": False, "right": False}
        self.collided = False
        self._speed = speed
        self._main_path = f"images\pokemon\{pokemon.get_name()}"
        self._animation_timer = 0
        self._walk_texture_num = 0

        self.hidden_visual = arcade.load_texture("images/transparent.png")

        self.idle_textures = {"up": None, "down": None,
                              "left": None, "right": None}
        for key in self.idle_textures:
            texture = arcade.load_texture(
                f"{self._main_path}\idle-{key}.png", scale=1.5)
            self.idle_textures[key] = texture

        self.walk_textures = {"up": [], "down": [],
                              "left": [], "right": []}
        for key in self.walk_textures.keys():
            texture1 = arcade.load_texture(
                f"{self._main_path}\walk-{key}0.png", scale=1.5)
            if key == "left" or key == "right":
                texture2 = arcade.load_texture(
                    f"{self._main_path}\idle-{key}.png", scale=1.5)
            else:
                texture2 = arcade.load_texture(
                    f"{self._main_path}\walk-{key}1.png", scale=1.5)
            self.walk_textures[key].append(texture1)
            self.walk_textures[key].append(texture2)

        if self.hidden:
            self.texture = self.hidden_visual
        else:
            self.texture = self.idle_textures[self._character_direction]

    def get_speed(self):
        return self._speed
    
    def set_speed(self, value: int):
        self._speed = value
    
    def get_movement(self):
        return self._movement
    
    def set_movement(self, direction: str, moving: bool):
        self._movement[direction] = moving
    
    def get_character_direction(self):
        return self._character_direction

    def set_boundaries(self, width: int, height: int):
        self.boundary_top = height
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = width

    def detected(self, detecting:str="player"):
        vision_field_x = list(range(int(self.left), int(self.right)))
        vision_field_y = list(range(int(self.bottom), int(self.top)))
        direction = self._character_direction
        detection_range = self._detection_range
        if detecting == "player":
            for player in Entity.player:
                if direction == "up":
                    if int(player.center_x) in vision_field_x and int(player.center_y) in range(int(self.center_y), int(self.top)+detection_range):
                        return True
                elif direction == "down":
                    if int(player.center_x) in vision_field_x and int(player.center_y) in range(int(self.bottom)-detection_range, int(self.center_y)):
                        return True
                elif direction == "left":
                    if int(player.center_y) in vision_field_y and int(player.center_x) in range(int(self.left)-detection_range, int(self.center_x)):
                        return True
                elif direction == "right":
                    if int(player.center_y) in vision_field_y and int(player.center_x) in range(int(self.center_x), int(self.right)+detection_range):
                        return True    

    def update(self):
        if self in Entity.enemy and self.hidden:
            if self.detected():
                self.texture = self.idle_textures[self._character_direction]
                self.hidden = False
                        
        if self.pokemon.get_hp() <= 0:
            self.remove_from_sprite_lists()

        if self._movement["up"] and self.top < self.boundary_top:
            self.change_y = self._speed
        elif self._movement["down"] and self.bottom > self.boundary_bottom:
            self.change_y = -self._speed
        else:
            self.change_y = 0

        if self._movement["left"] and self.left > self.boundary_left:
            self.change_x = -self._speed
        elif self._movement["right"] and self.right < self.boundary_right:
            self.change_x = self._speed
        else:
            self.change_x = 0

        self.position = [self._position[0] + self.change_x, self._position[1] + self.change_y]

    def update_animation(self, delta_time: float = 1/60):
        if not self.hidden:
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

            if self.change_x < 0:
                self._character_direction = "left"
                self.texture = self.walk_textures["left"][self._walk_texture_num]
                self._animation_timer += 1
            elif self.change_x > 0:
                self._character_direction = "right"
                self.texture = self.walk_textures["right"][self._walk_texture_num]
                self._animation_timer += 1
            elif self.change_y < 0:
                self._character_direction = "down"
                self.texture = self.walk_textures["down"][self._walk_texture_num]
                self._animation_timer += 1
            elif self.change_y > 0:
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

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name.lower()

    def get_items(self):
        return self._items

    def remove_item(self, item: str, amount: int):
        self._items[item.capitalize()] -= amount

    def get_pokemons(self):
        return self._pokemons


class Player(Trainer):
    def __init__(self, name, pokemons, items=None, money=None):
        super().__init__(name, pokemons, items=items, money=money)
        self._money = money

    def add_item(self, item: str, amount: int):
        self._items[item.capitalize()] += amount

    def get_money(self):
        return self._money

    def set_money(self, money: int):
        self._money = money

    def add_money(self, amount: int):
        self._money += amount

    def subtract_money(self, amount: int):
        self._money -= amount

    def add_pokemon(self, pokemon: Pokemon):
        if len(self._pokemons) <= 6:
            self._pokemons.append(pokemon)
        else:
            return ValueError("Too many pokemon. Max: 6")  # place in pc

    def release_pokemon(self, name: str):
        if len(self._pokemons) == 1:
            return ValueError("Cannot remove last pokemon. Min: 1")
        else:
            for i in range(self._pokemons):
                if self._pokemons[i].get_name == name.lower():
                    del self._pokemons[i]


# class PC():
    def __init__(self):
        self._stored = {}
        self._pages = []

        for page in range(20):
            for i in range(100):
                self._stored[i] = None
            self._pages[page] = self._stored

    def add_pokemon(self, page_number: int, place_number: int, pokemon: Pokemon):
        for empty in self._stored[page_number]:
            pass


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

    def attack(self, pokemon: object, ability, opponent: object):
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


    return new_array
