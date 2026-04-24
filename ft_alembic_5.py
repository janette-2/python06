from alchemy import create_air


if __name__ == "__main__":
    print("=== Alembic 5 ===")
    print("Accessing alchemy module using 'from alchemy import ...'")

    # directly access to the function imported
    print(f"Testing create_air: {create_air()}")
