# import the entire file of the directory
import alchemy.elements
# directly access to the directory's file (dir.file)
# and then the function


if __name__ == "__main__":
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using: 'import ...' structure")

    # direct import structure and access to the import
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")
