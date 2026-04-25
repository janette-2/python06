from . import light_validator
# NEEDS RELATIVE IMPORT BECAUSE light_validator IS NOT A SEPARATE
# MODULE WITH IT'S OWN __init__.py, THOSE ARE THE ONLY TIMES YOU CAN
# USE ABSOLUTE IMPORTS [DIRECT IMPORTS] (import aclhemy.grimoire)
# BECAUSE THEY HAVE: [package -> init -> absolute import]


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    val = light_validator.validate_ingredients(ingredients)

    if "INVALID" in val:
        res = f"Spell rejected: {spell_name} ({val})"
        return res

    res = f"Spell recorded: {spell_name} ({val})"
    return res


# TEST
if __name__ == "__main__":
    print(f"Testing record light spell: "
          f"{light_spell_record("Name", "aaa, AIR")}")
