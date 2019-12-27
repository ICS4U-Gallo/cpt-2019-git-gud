from typing import List, Dict
import random as r
from settings import ITEMS, MONEY


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


class PC(): # IN PROGRESS
    # Set dict on each screen
    # when dict is full, move to next screen
    # searches and whatnot can be implemented afterwards
    def __init__(self, pc_pokemons: Dict[int, Pokemon]):
        self._stored = pc_pokemons
        self._pages = {}
        
        for page in range(20):
            for i in range(100):
                self._stored[i] = "" # THE ERROR IS THAT IT CHANGES POKEMON INTO A STRING
            self._pages[page] = self._stored


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
    def __init__(self, name: str, hp: int, type: str, lvl: int,
                 attack_one: str, attack_one_power: int, attack_one_type: str,
                 attack_one_audio: str = None, pokemon_pic: str = None,
                 pokemon_sound: str = None, passive: str = None):
        super().__init__(attack_one, attack_one_power,
                         attack_one_type, attack_one_audio)
        self._name = name.lower()
        self._hp = hp
        self._type = type.lower()
        self._lvl = lvl
        self._attack_counter = 1
        self._pokemon_pic = pokemon_pic
        self._pokemon_sound = pokemon_sound
        self._passive = passive
        self._item = None

    def set_name(self, name: str):
        self._name = name.lower()

    def get_name(self):
        return self._name

    def set_hp(self, hp: int):
        self._hp = hp

    def get_hp(self):
        return self._hp

    def set_type(self, type: str):
        self._type = type.lower()

    def get_type(self):
        return self._type

    def set_lvl(self, lvl: int):
        self._lvl = lvl

    def get_lvl(self):
        return self._lvl

    def set_passive(self, passive: str):
        self._passive = passive.lower()

    def get_passive(self):
        return self._passive

    def set_item(self, item: str):
        self._item = item.capitalize()

    def get_item(self):
        return self._item

    def set_pokemon_pic(self, file: str):
        self._pokemon_pic = file

    def get_pokemon_pic(self):
        return self._pokemon_pic

    def set_pokemon_sound(self, audio: str):
        self._pokemon_sound = audio

    def get_pokemon_sound(self):
        return self._pokemon_sound

    def add_attack(self, attack: str, power: int,
                   type: str, audio=None):
        if len(Attack.attacks) <= 4:
            super().__init__(attack, power, type, audio)
        else:
            raise ValueError("Maximum attacks reached. Max: 4")

    def get_attack(self, attack: int):
        return Attack.attacks[attack]

    def attack(self, enemy: str):
        pass


class Strengths(): # IN PROGRESS
    def __init__(self, your_type: str):
        self._type = your_type.lower()
        self._bug = ["grass", "dark", "psychic"]
        self._dark = ["ghost", "psychic"]
        self._dragon = ["dragon"]
        self._electric = ["flying", "water"]
        self._fairy = ["fighting", "dark", "dragon"]
        self._fighting = ["dark", "ice", "normal", "steel"]
        self._fire = ["bug", "grass", "ice", "steel"]
        self._flying = ["bug", "fighting", "grass"]
        self._ghost = ["ghost", "psychic"]
        self._grass = ["ground", "rock", "water"]
        self._ground = ["electric", "fire", "poison", "rock", "steel"]
        self._ice = ["dragon", "flying", "grass", "ground"]
        self._normal = []
        self._poison = ["fairy", "grass"]
        self._psychic = ["fighting", "poison"]
        self._rock = ["bug", "fire", "flying", "ice"]
        self._steel = ["fairy", "ice", "rock"]
        self._water = ["fire", "ground", "rock"]

    def bug(self, enemy_type: str):
        for Type in range(self._bug):
            if enemy_type.lower() == Type:
                return True
        return False

    def dark(self, enemy_type: str):
        for Type in range(self._dark):
            if enemy_type.lower() == Type:
                return True
        return False

    def dragon(self, enemy_type: str):
        for Type in range(self._dragon):
            if enemy_type.lower() == Type:
                return True
        return False

    def electric(self, enemy_type: str):
        for Type in range(self._electric):
            if enemy_type.lower() == Type:
                return True
        return False

    def fairy(self, enemy_type: str):
        for Type in range(self._fairy):
            if enemy_type.lower() == Type:
                return True
        return False

    def fighting(self, enemy_type: str):
        for Type in range(self._fighting):
            if enemy_type.lower() == Type:
                return True
        return False

    def fire(self, enemy_type: str):
        for Type in range(self._fire):
            if enemy_type.lower() == Type:
                return True
        return False

    def flying(self, enemy_type: str):
        for Type in range(self._flying):
            if enemy_type.lower() == Type:
                return True
        return False

    def ghost(self, enemy_type: str):
        for Type in range(self._ghost):
            if enemy_type.lower() == Type:
                return True
        return False

    def grass(self, enemy_type: str):
        for Type in range(self._grass):
            if enemy_type.lower() == Type:
                return True
        return False

    def ground(self, enemy_type: str):
        for Type in range(self._ground):
            if enemy_type.lower() == Type:
                return True
        return False

    def ice(self, enemy_type: str):
        for Type in range(self._ice):
            if enemy_type.lower() == Type:
                return True
        return False

    def normal(self, enemy_type: str):
        for Type in range(self.normal):
            if enemy_type.lower() == Type:
                return True
        return False

    def poison(self, enemy_type: str):
        for Type in range(self._poison):
            if enemy_type.lower() == Type:
                return True
        return False

    def psychic(self, enemy_type: str):
        for Type in range(self._psychic):
            if enemy_type.lower() == Type:
                return True
        return False

    def rock(self, enemy_type: str):
        for Type in range(self._rock):
            if enemy_type.lower() == Type:
                return True
        return False

    def steel(self, enemy_type: str):
        for Type in range(self._steel):
            if enemy_type.lower() == Type:
                return True
        return False

    def water(self, enemy_type: str):
        for Type in range(self._water):
            if enemy_type.lower() == Type:
                return True
        return False

    def strength(self, enemy_type: str):
        if self._type == "bug":
            return self.bug(enemy_type)
        elif self._type == "dark":
            return self.dark(enemy_type)
        elif self._type == "dragon":
            return self.dragon(enemy_type)
        elif self._type == "electric":
            return self.electric(enemy_type)
        elif self._type == "fairy":
            return self.fairy(enemy_type)
        elif self._type == "fighting":
            return self.fighting(enemy_type)
        elif self._type == "fire":
            return self.fire(enemy_type)
        elif self._type == "flying":
            return self.flying(enemy_type)
        elif self._type == "ghost":
            return self.ghost(enemy_type)
        elif self._type == "grass":
            return self.grass(enemy_type)
        elif self._type == "ground":
            return self.ground(enemy_type)
        elif self._type == "ice":
            return self.ice(enemy_type)
        elif self._type == "normal":
            return self.ice(enemy_type)
        elif self._type == "poison":
            return self.poison(enemy_type)
        elif self._type == "psychic":
            return self.psychic(enemy_type)
        elif self._type == "rock":
            return self.rock(enemy_type)
        elif self._type == "steel":
            return self.steel(enemy_type)
        elif self._type == "water":
            return self.water(enemy_type)
        else:
            return "not here"


class Weaknesses(): #IN PROGRESS
    def __init__(self, your_type: str):
        self._type = your_type.lower()
        self._bug = ["fire", "flying", "rock"]
        self._dark = ["bug", "fairy", "fighting"]
        self._dragon = ["dragon", "fairy", "ice"]
        self._electric = ["ground"]
        self._fairy = ["poison", "steel"]
        self._fighting = ["fairy", "flying", "psychic"]
        self._fire = ["ground", "rock", "water"]
        self._flying = ["electric", "ice", "rock"]
        self._ghost = ["dark", "ghost"]
        self._grass = ["bug", "fire", "flying", "ice",  "poison"]
        self._ground = ["grass", "ice", "water"]
        self._ice = ["fighting", "fire", "rock", "steel"]
        self._normal = ["fighting"]
        self._poison = ["ground", "psychic"]
        self._psychic = ["bug", "dark", "ghost"]
        self._rock = ["fighting", "grass", "ground", "steel", "water"]
        self._steel = ["fighting", "fire", "ground"]
        self._water = ["electric", "grass"]

    def bug(self, enemy_type: str):
        for Type in range(self._bug):
            if enemy_type.lower() == Type:
                return True
        return False

    def dark(self, enemy_type: str):
        for Type in range(self._dark):
            if enemy_type.lower() == Type:
                return True
        return False

    def dragon(self, enemy_type: str):
        for Type in range(self._dragon):
            if enemy_type.lower() == Type:
                return True
        return False

    def electric(self, enemy_type: str):
        for Type in range(self._electric):
            if enemy_type.lower() == Type:
                return True
        return False

    def fairy(self, enemy_type: str):
        for Type in range(self._fairy):
            if enemy_type.lower() == Type:
                return True
        return False

    def fighting(self, enemy_type: str):
        for Type in range(self._fighting):
            if enemy_type.lower() == Type:
                return True
        return False

    def fire(self, enemy_type: str):
        for Type in range(self._fire):
            if enemy_type.lower() == Type:
                return True
        return False

    def flying(self, enemy_type: str):
        for Type in range(self._flying):
            if enemy_type.lower() == Type:
                return True
        return False

    def ghost(self, enemy_type: str):
        for Type in range(self._ghost):
            if enemy_type.lower() == Type:
                return True
        return False

    def grass(self, enemy_type: str):
        for Type in range(self._grass):
            if enemy_type.lower() == Type:
                return True
        return False

    def ground(self, enemy_type: str):
        for Type in range(self._ground):
            if enemy_type.lower() == Type:
                return True
        return False

    def ice(self, enemy_type: str):
        for Type in range(self._ice):
            if enemy_type.lower() == Type:
                return True
        return False

    def normal(self, enemy_type: str):
        for Type in range(self.normal):
            if enemy_type.lower() == Type:
                return True
        return False

    def poison(self, enemy_type: str):
        for Type in range(self._poison):
            if enemy_type.lower() == Type:
                return True
        return False

    def psychic(self, enemy_type: str):
        for Type in range(self._psychic):
            if enemy_type.lower() == Type:
                return True
        return False

    def rock(self, enemy_type: str):
        for Type in range(self._rock):
            if enemy_type.lower() == Type:
                return True
        return False

    def steel(self, enemy_type: str):
        for Type in range(self._steel):
            if enemy_type.lower() == Type:
                return True
        return False

    def water(self, enemy_type: str):
        for Type in range(self._water):
            if enemy_type.lower() == Type:
                return True
        return False

    def weaknesses(self, enemy_type: str):
        if self._type == "bug":
            return self.bug(enemy_type)
        elif self._type == "dark":
            return self.dark(enemy_type)
        elif self._type == "dragon":
            return self.dragon(enemy_type)
        elif self._type == "electric":
            return self.electric(enemy_type)
        elif self._type == "fairy":
            return self.fairy(enemy_type)
        elif self._type == "fighting":
            return self.fighting(enemy_type)
        elif self._type == "fire":
            return self.fire(enemy_type)
        elif self._type == "flying":
            return self.flying(enemy_type)
        elif self._type == "ghost":
            return self.ghost(enemy_type)
        elif self._type == "grass":
            return self.grass(enemy_type)
        elif self._type == "ground":
            return self.ground(enemy_type)
        elif self._type == "ice":
            return self.ice(enemy_type)
        elif self._type == "normal":
            return self.ice(enemy_type)
        elif self._type == "poison":
            return self.poison(enemy_type)
        elif self._type == "psychic":
            return self.psychic(enemy_type)
        elif self._type == "rock":
            return self.rock(enemy_type)
        elif self._type == "steel":
            return self.steel(enemy_type)
        elif self._type == "water":
            return self.water(enemy_type)


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
            return ValueError("Too many pokemon. Max: 6") #place in pc

    def release_pokemon(self, name: str):
        if len(self._pokemons) == 1:
            return ValueError("Cannot remove last pokemon. Min: 1")
        else:
            for i in range(self._pokemons):
                if self._pokemons[i].get_name == name.lower():
                    del self._pokemons[i]


class CPU(Trainer): # IN PROGRESS
    def __init__(self, name:  str, pokemons: List[Pokemon],
                 items: Dict[str, int] = None):
        super().__init__(name, pokemons, items)

    def normal(self, special: bool):
        if special:
            pass


class Battle(): # IN PROGRESS
    turns = 0

    def __init__(self, player: Player, cpu: CPU = None, wild_pokemon: Pokemon = None):
        self._player = player
        self._cpu = cpu
        self._wild_pokemon = wild_pokemon

    def catch(self, enemy_hp: int): # APPEND TO PC IF CAUGHT AND POKESLOTS ARE FULL
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
                if r.randint(1, 100) <=  90:
                    return True
                return False
            else:
                return True


def main():
    SQUIRTLE = Pokemon("Squirtle", 100, "water", 100, True,
                       "Bubble gun", 20, "water")
    CHARAMANDER = Pokemon("Charamander", 120, False, "fire",
                          80, "Flamethrower", 40, "fire")
    BULBASUAR = Pokemon("Bulbasuar", 110, True, "grass",
                        90, "Vine whip", 30, "grass")

    print(CHARAMANDER._name)
    print(CHARAMANDER._attack)
    print(SQUIRTLE._name)
    print(SQUIRTLE.get_name)
    print(SQUIRTLE.get_attack)
    SQUIRTLE.set_name("SQUIRT")
    print(SQUIRTLE._name)
    print(BULBASUAR.get_passive)

    print(BULBASUAR.get_item)

    POKEMONS = [SQUIRTLE, CHARAMANDER, BULBASUAR]

    jeff = Player("jeff", ITEMS, POKEMONS, MONEY)

    print(jeff.get_pokemons)


if __name__ == "__main__":
    main()
