from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    val = validate_ingredients(ingredients)

    if "INVALID" in val:
        res = f"Spell rejected: {spell_name} ({val})"
        return res

    res = f"Spell recorded: {spell_name} ({val})"
    return res


# TEST
if __name__ == "__main__":
    print(f"Testing record dark spell: "
          f"{dark_spell_record("Name", "aaa, AIR")}")
