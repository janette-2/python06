def validate_ingredients(ingredients: str) -> str:
    # LOCAL IMPORT to avoid circular dependencies explosion
    from . import light_spellbook
    valid = light_spellbook.light_spell_allowed_ingredients()
    for val in valid:
        # Looks for at least one coincidence (in lower case to match valids)
        #  of the valid ones in 'ingredients'(transformed) if found,
        #  'ingredients' as a whole is valid.
        if val in ingredients.lower():
            return ingredients + "- VALID"
    # else..
    return ingredients + "- INVALID"
