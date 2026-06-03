def choose_class():
    classes = ["Warrior", "Mage", "Rogue"]
    print("Available Classes:", ", ".join(classes))
    choice = input("Choose your class: ").capitalize()
    return choice if choice in classes else "Adventurer"

def get_starting_gear(char_class):
	gear = {
	"Warrior": ["Iron Sword", "Shield"],
	"Mage": ["Staff", "Mana Potion"],
	"Rogue": ["Daggers", "Smoke Bomb"]
}
return gear.get(char_class, ["Ragged Clothes"])

def main():
    print("--- Welcome to the Character Generator ---")
    name = input("Enter character name: ")
    gear = get_starting_gear("Warrior")
    print(f"\nCharacter {name} created with gear: {gear}!")

if __name__ == "__main__":
    main()