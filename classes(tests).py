class Player(Pokemon):
    def __init__(self, name, health_points, Type, passive_ability, moveset, image, level=1):
        super().__init__(name, health_points, Type, passive_ability, moveset, image, level=level)
        x = 0
        y = 0

class Shadow(Pokemon):
    def __init__(self, name, health_points, Type, passive_ability, moveset, image, level=1):
        super().__init__(name, health_points, Type, passive_ability, moveset, image, level=level)