# Imported like: dark_spellbook -> dark_validator
# dark_validatoR -> dark_spellbook ##CIRCULAR DEPENDENCY, EXPLODES##
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    valid = dark_spell_allowed_ingredients()
    for val in valid:
        # Looks for at least one coincidence (in lower case to match valids)
        #  of the valid ones in 'ingredients'(transformed) if found,
        #  'ingredients' as a whole is valid.
        if val in ingredients.lower():
            return ingredients + "- VALID"
    # else..
    return ingredients + "- INVALID"
