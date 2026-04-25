if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire.dark_spellbook import dark_spell_record
    # IF THE IMPORT IS NOT INSIDE THE MODULE(out of __name__=__main__) FLAKE8
    # DOOESN'T DETECT THE ERRORS

    print(f"{dark_spell_record("Fantasy", "Earth, water and air")}")
