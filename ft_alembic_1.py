# import from a file in the same directory but selecting
#  which elements to import
from elements import create_water

if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...'' structure to access elements.py")

    # directly access to the function imported
    print(f"Testing create_water: {create_water()}")
