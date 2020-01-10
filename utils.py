from typing import List, Dict
import random as r
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


class Pokemon:
    def __init__(self, name, health_points, Type, passive_ability, moveset,
                 image, sound, level, experience_points=0, item=None):
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


class PC():  # IN PROGRESS
    # Set dict on each screen
    # when dict is full, move to next screen
    # searches and whatnot can be implemented afterwards
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


    def catch(self, enemy_hp: int):  # APPEND TO PC IF CAUGHT AND POKESLOTS ARE FULL
        if self._wild_pokemon != None:
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

def bubble_sort(array):
    while True:
        changed = False
        for i in range(len(array)):
            if i != len(array) - 1:
                current = array[i]
                proceeding = array[i+1]
                if current > proceeding:
                    array[i] = proceeding
                    array[i+1] = current
                    changed = True
        if not changed:
            return array