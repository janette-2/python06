from ..elements import create_air  # From the last level (alchemy)
from elements import create_fire  # From the root
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    f = ("Recipe transmuting Lead to Gold: brew "
         f"’{create_air()}’ and ’{strength_potion()}’ mixed"
         f" with ’{create_fire()}’")
    return f
