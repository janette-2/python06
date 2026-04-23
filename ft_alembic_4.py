import alchemy.elements

alchemy.elements.create_air()
# ¿COMO SE HARÍA LA PARTE DEL create_earth()?


def main() -> None:
    # The type ignore will make sure that mypy
    # doesn't detect errors on the problematic element
    print(f"{alchemy.elements.create_earth()}")  # type: ignore
    raise AttributeError("AttributeError: module 'alchemy' has no attribute"
                         " 'create_earth'. Did you mean: 'create_air'?")


if __name__ == "__main__":
    main()
