def main():
print("---Welcome to the Welcome to the Character Generator ---")
    # Components will be combined here
    name = "Hero"
    print(f"\nCharacter {name} has been successfully created!")

if __name__ == "__main__":
    main()
# ========================================
# ATTRIBUTE ROLLER - Person A
# ========================================

import random

def roll_attributes():
    """Rolls random stats for Strength, Agility, and Intellect"""
    return {
        "Strength": random.randint(5, 20),
        "Agility": random.randint(5, 20),
        "Intellect": random.randint(5, 20)
    }


# Example usage in main (temporary)
if __name__ == "__main__":
    print("--- Welcome to the Character Generator ---")
    attributes = roll_attributes()
    print("\nRolled Attributes:")
    for stat, value in attributes.items():
        print(f"  {stat}: {value}")
