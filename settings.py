import arcade
from typing import List, Dict

WIDTH = 800
HEIGHT = 600
load_saves = False
info = None
BACKGROUND = arcade.load_texture("images/screen_menu_background.png")
MALE_CHAR = arcade.load_texture("images/char_male.png")
FEMALE_CHAR = arcade.load_texture("images/char_female.png")
BACKGROUND_MUSIC = arcade.load_sound("audio/screen_menu.mp3")
RING = arcade.load_sound("audio/menu_get.mp3")
BATTLE_BACKGROUND = arcade.load_texture("images/battle_background.png")
CHAR = ""
NAME = ""
ITEMS = {"Pokeballs":  0,
         "Potions":  0,
         "Paralysis antidote": 0,
         "Poison antidote": 0,
         "Strength pill": 0,
         "Speed pill": 0,
         "Defense pill": 0,
         "Elemental pill": 0,
         "Berries": 0}
MONEY = 0

strengths = {"bug": ["grass", "dark", "psychic"], "dark": ["ghost", "psychic"],
             "dragon": ["dragon"], "electric": ["flying", "water"], "fairy": ["fighting", "dark", "dragon"],
             "fighting": ["dark", "ice", "normal", "steel"], "fire": ["bug", "grass", "ice", "steel"],
             "flying": ["bug", "fighting", "grass"], "ghost": ["ghost", "psychic"],
             "grass": ["ground", "rock", "water"], "ground": ["electric", "fire", "poison", "rock", "steel"],
             "ice": ["dragon", "flying", "grass", "ground"], "normal": [], "poison": ["fairy", "grass"],
             "psychic": ["fighting", "poison"], "rock": ["bug", "fire", "flying", "ice"],
             "steel": ["fairy", "ice", "rock"], "water": ["fire", "ground", "rock"]}
weaknesses = {"bug": ["fire", "flying", "rock"], "dark": ["bug", "fairy", "fighting"],
              "dragon": ["dragon", "fairy", "ice"], "electric": ["ground"], "fairy": ["poison", "steel"],
              "fighting": ["fairy", "flying", "psychic"], "fire": ["ground", "rock", "water"],
              "flying": ["electric", "ice", "rock"], "ghost": ["dark", "ghost"],
              "grass": ["bug", "fire", "flying", "ice", "poison"], "ground": ["grass", "ice", "water"],
              "ice": ["fighting", "fire", "rock", "steel"], "normal": ["fighting"], "poison": ["ground", "psychic"],
              "psychic": ["bug", "dark", "ghost"], "rock": ["fighting", "grass", "ground", "steel", "water"],
              "steel": ["fighting", "fire", "ground"], "water": ["electric", "grass"]}
CHARACTERS = "abcdefghijklmnopqrstuvwxyz,.!?@#$%&*"
