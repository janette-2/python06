import elements
from . import elements as al_elements


def healing_potion() -> str:
    f = (f"Healing potion brewed with '{al_elements.create_earth()}'"
         f" and '{al_elements.create_air()}'")
    return f


def strength_potion() -> str:
    f = ("Strength potion brewed"
         f" with ’{elements.create_fire()}’ and ’{elements.create_water()}'")
    return f
