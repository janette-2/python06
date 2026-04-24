import alchemy


if __name__ == "__main__":
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print("Testing lead to gold: "
          # Variable declared in the transmutation module (__init__) to
          #  execute the function when the module is imported
          f"{alchemy.lead_to_gold}")
