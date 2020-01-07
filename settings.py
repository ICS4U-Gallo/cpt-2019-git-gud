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
