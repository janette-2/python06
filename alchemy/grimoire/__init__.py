from . import light_validator
from . import light_spellbook
# ALWAYS IMPORTS INTERN MODULES -> from . import <module>

# EXPOSES FUNCTIONS TO THE OUTSIDE AS...
validate_ingredients = light_validator.validate_ingredients
light_spell_record = light_spellbook.light_spell_record

# DEFINES WHAT ELEMENTS FROM THIS PACKAGE CAN BE ACCESSED BY ALL...
__all__ = ["validate_ingredients", "light_spell_record"]
