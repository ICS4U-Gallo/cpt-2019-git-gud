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
class Attack():
    def __init__(attack: str, attack_audio: str, attack_power: int, type: str):
        pass

class Pokemon(Attack):
    def __init__(self, name: str, hp: int, ap: int, type: str, lvl: int,
                 attack_one: str, attack_one_audio: str = None,
                 pokemon_pic: str = None, pokemon_sound: str = None,
                 passive: str = None):
        self._name = name
        self._hp = hp
        self._ap = ap
        self._type = type
        self._lvl = lvl
        self._attack_counter = 1
        self._attack_one = attack_one
        self._attack_two = None
        self._attack_three = None
        self._attack_four = None
        self._attack_one_audio = attack_one_audio
        self._attack_two_audio = None
        self._attack_three_audio = None
        self._attack_four_audio = None
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

    def set_ap(self, ap: int):
        self._ap  = ap
    
    def get_ap(self):
        return self._ap
    
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

    def set_attack_one(self, attack: str):
        self._attack_one = attack
    
    def get_attack_one(self):
        return self._attack_one

    def set_attack_two(self, attack: str):
        self._attack_two = attack
    
    def get_attack_two(self):
        return self._attack_two
    
    def set_attack_three(self, attack: str):
        self._attack_three = attack
        
    def get_attack_three(self):
        return self._attack_three

    def set_attack_four(self, attack: str):
        self._attack_four = attack
        
    def get_attack_four(self):
        return self._attack_four
    
    def set_attack_one_audio(self, audio: str):
        self._attack_one_audio = audio
    
    def get_attack_one_audio(self):
        return self._attack_one_audio

    def set_attack_two_audio(self, audio: str):
        self._attack_two_audio = audio
    
    def get_attack_two_audio(self):
        return self._attack_two_audio
    
    def set_attack_three_audio(self, audio: str):
        self._attack_three_audio = audio
    
    def get_attack_three_audio(self):
        return self._attack_three_audio

    def set_attack_four_audio(self, audio:  str):
        self._attack_four_audio = audio
    
    def get_attack_four_audio(self):
        return self._attack_four_audio
    
    def set_pokemon_pic(self, file: str):
        self._pokemon_pic = file
    
    def get_pokemon_pic(self):
        return self._pokemon_pic
    
    def set_pokemon_sound(self, audio: str):
        self._pokemon_sound  = audio
    
    def get_pokemon_sound(self):
        return self._pokemon_sound
    
    def add_attack(self, attack: str, audio=None):
        if self._attack_counter == 1:
            self.set_attack_two(attack)
            self.set_attack_one_audio(audio)
            self._attack_counter += 1
        elif self._attack_counter == 2:
            self.set_attack_three(attack)
            self.set_attack_three_audio(audio)
            self._attack_counter += 1
        elif self._attack_counter == 3:
            self.set_attack_four(attack)
            self.set_attack_four_audio(audio)
        else:
            return ValueError("Too many attacks")


class Player():
    def __init__(self, name: str, items: Dict[str, int],
                 pokemons: List[Pokemon]):
        self._name = name
        self._items = items
        self._pokemons = pokemons
        
    def set_name(self, name: str):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def get_items(self):
        return self._items
    
    def add_item(self, item: str, amount: int):
        self._items[item] += amount
    
    def use_item(self, item: str, amount: int):
        self._items[item] -= amount
        
    def get_pokemons(self):
        return self._pokemons
