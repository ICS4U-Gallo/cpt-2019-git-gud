import arcade
from typing import List, Dict

WIDTH = 800
HEIGHT = 600
save_info = None
BACKGROUND = arcade.load_texture("images/screen_menu_background.png")
MALE_CHAR = arcade.load_texture("images/char_male.png")
FEMALE_CHAR = arcade.load_texture("images/char_female.png")
BACKGROUND_MUSIC = arcade.load_sound("audio/screen_menu.mp3")
RING = arcade.load_sound("audio/menu_get.mp3")
CHAR = ""
NAME = ""
ITEMS = {"Pokeballs":  0,
         "Potions":  0,
         "Paralysis Antidote": 0,
         "Poison Antidote": 0,
         "Strength Pill": 0,
         "Speed Pill": 0,
         "Defense Pill": 0,
         "Elemental Pill": 0,
         "Berries": 0}
MONEY = 0


class Attack():
    attacks = []
    def __init__(self, attack: str, attack_power: int,
                 type: str, attack_audio: str = None):
        self._attack = attack
        self._attack_power = attack_power
        self._attack_type = type
        self._attack_audio = attack_audio
        Attack.attacks.append(self)
        
    def set_attack(self, attack: str):
        self._attack = attack
        
    def get_attack(self):
        return self._attack
    
    def set_attack_power(self, attack_power: int):
        self._attack_power = attack_power
    
    def get_attack_power(self):
        return self._attack_power
    
    def set_attack_type(self, type: str):
        self._attack_type = type
        
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
        self._name = name
        self._hp = hp
        self._type = type
        self._lvl = lvl
        self._attack_counter = 1
        self._pokemon_pic = pokemon_pic
        self._pokemon_sound = pokemon_sound
        self._passive = passive
        self._item = None        

    def set_name(self, name: str):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_hp(self, hp: int):
        self._hp = hp
    
    def get_hp(self):
        return self._hp
    
    def set_type(self, type: str):
        self._type = type
    
    def get_type(self):
        return self._type

    def set_lvl(self, lvl: int):
        self._lvl = lvl
        
    def get_lvl(self):
        return self._lvl
    
    def set_passive(self, passive):
        self._passive = passive

    def get_passive(self):
        return self._passive

    def set_item(self, item: str):
        self._item = item
        
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
    
    def add_attack(self, attack: str, power: int, type: str, audio=None):
        if len(Attack.attacks) <= 4:
            super().__init__(attack, power, type, audio)
        else:
            raise ValueError("Maximum attacks reached. Max: 4")
        
    def get_attack(self, attack: int):
        return Attack.attacks[attack]


class Player():
    def __init__(self, name: str, items: Dict[str, int],
                 pokemons: List[Pokemon], money: int):
        self._name = name
        self._items = items
        self._pokemons = pokemons
        self._money = money
        
    def set_name(self, name: str):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def get_items(self):
        return self._items
    
    def add_item(self, item: str, amount: int):
        self._items[item] += amount
    
    def remove_item(self, item: str, amount: int):
        self._items[item] -= amount
        
    def set_money(self, money: int):
        self._money = money
    
    def get_money(self):
        return self._money

    def add_money(self, amount: int):
        self._money += amount
    
    def subtract_money(self, amount: int):
        self._money -= amount
        
    def get_pokemons(self):
        return self._pokemons
            
    def add_pokemon(self, pokemon: Pokemon):
        if len(self._pokemons) < 6:
            self._pokemons.append(pokemon)
        else:
            return ValueError("Too many pokemon. Max: 6")
    
    def remove_pokemon(self, name: str):
        if len(self._pokemons) == 1:
            return ValueError("Cannot remove last pokemon. Min: 1")
        else:
            for i in range(self._pokemons):
                if self._pokemons[i].get_name == name:
                    del self._pokemons[i]


SQUIRTLE = Pokemon("Squirtle", 100, "water", 100, "Bubble gun", 20, "water")
CHARAMANDER = Pokemon("Charamander", 120, "fire", 80, "Flamethrower", 40, "fire")
BULBASUAR = Pokemon("Bulbasuar", 110, "grass", 90, "Vine whip", 30, "grass")

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
