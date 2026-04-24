import alchemy.transmutation as transmutation


if __name__ == "__main__":
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print("Testing lead to gold: "
          # Variable declared in the transmutation module (__init__) to
          #  execute the function when the module is imported
          f"{transmutation.lead_to_gold}")
