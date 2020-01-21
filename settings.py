import arcade
import utils
from typing import List, Dict

WIDTH = 800
HEIGHT = 600
shown = False
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
POKEMONS = []

SQUIRTLE = utils.Pokemon("Squirtle", 1200, "water", "rain dance", "", "", 20)
SQUIRTLE.add_attack("bubble beam", 40, "water")
SQUIRTLE.add_attack("hydro pump", 120, "water")
SQUIRTLE.add_attack("scratch", 70, "normal")
SQUIRTLE.add_attack("shell tackle", 90, "fighting")
CHARAMANDER = utils.Pokemon("Charamander", 650, "fire", "fired up", "", "", 17)
CHARAMANDER.add_attack("flamethrower", 100, "fire")
CHARAMANDER.add_attack("scratch", 40, "normal")
CHARAMANDER.add_attack("fire tail", 70, "fire")
CHARAMANDER.add_attack("PSYCHIC", 130, "psychic")
BULBASAUR = utils.Pokemon("Bulbasaur", 1000, "grass", "grassy field", "", "", 19)
BULBASAUR.add_attack("vine whip", 110, "grass")
BULBASAUR.add_attack("grass blades", 20, "grass")
BULBASAUR.add_attack("solar beam", 200, "psychic")
BULBASAUR.add_attack("earthquake", 150, "ground")
PIKACHU = utils.Pokemon("Pikachu", 427, "electric", "shocking", "", "", 15)
PIKACHU.add_attack("lightning bolt", 100, "electric")
PIKACHU.add_attack("volt tackle", 230, "electric")
PIKACHU.add_attack("tackle", 60, "electric")
PIKACHU.add_attack("iron tail", 80, "normal")
CHEERIO = utils.Pokemon("Cheerio", 1000000, "fighting", "owie", "", "", 42)
CHEERIO.add_attack("scratch", 200, "normal")
CHEERIO.add_attack("crunch", 150, "dark")
CHEERIO.add_attack("taunt", 20, "normal")
CHEERIO.add_attack("glare", 110, "ghost")
BUTTER = utils.Pokemon("Butter", 1, "normal", "slippy slide", "", "", 30)
BUTTER.add_attack("slip", 400, "fighting")
BUTTER.add_attack("slide", 450, "normal")
BUTTER.add_attack("melt", 200, "water")
BUTTER.add_attack("harden", 500, "ice")
POKEMONS.append(SQUIRTLE)
POKEMONS.append(CHARAMANDER)
POKEMONS.append(BULBASAUR)
POKEMONS.append(PIKACHU)
POKEMONS.append(CHEERIO)
POKEMONS.append(BUTTER)
PLAYER_ITEMS = {"Pokeballs":  20,
         "Potions":  30,
         "Paralysis antidote": 5,
         "Poison antidote": 7,
         "Strength pill": 10,
         "Speed pill": 12,
         "Defense pill": 17,
         "Elemental pill": 20,
         "Berries": 40}
# PLAYER = utils.Player("Sir Gallo", POKEMONS, PLAYER_ITEMS, 3000)
# ENEMY = utils.Player("Sir Fabroa", POKEMONS, PLAYER_ITEMS, 1000)

# THE_BATTLE = utils.Battle(PLAYER, ENEMY)

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
