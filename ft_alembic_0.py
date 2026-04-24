# import functions from a file that is located in the same directory
import elements

if __name__ == "__main__":
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")

    # direct import structure and access to the import
    print(f"Testing create_fire: {elements.create_fire()}")
