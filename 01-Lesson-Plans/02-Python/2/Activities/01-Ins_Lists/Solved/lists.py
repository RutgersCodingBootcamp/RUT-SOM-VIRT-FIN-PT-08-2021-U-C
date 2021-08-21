# -*- coding: utf-8 -*-
"""
Instructor Demo: Lists.

This script showcases basic operations of Python Lists.
"""

# Cheer-leading python exercise
# Create a variable named cheer
cheer = ["Python", "FinTech","Money"]

# Below strings can be used to add fun
cheer_symbol = "*\O/*"
cheer_symbol_2 = "ヘ( ^o^)ノ＼(^_^ )"

# Loop through string
for i in range(len(cheer)):
    for x in cheer[i]:
        #Print each letter with a cheer
        print("Give me a " + x + "!")
        print(x + "!")

    # Print excitement to screen
    print("\nWhat does that spell?!")
    print(cheer[i] + "!\nWoohoo! Go " + cheer[i] + "!")
    print(cheer_symbol * 3)
    print(cheer_symbol_2)
    print()

# Create a list of Pokemon
print("Creating a list of Pokemon...")
pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Gyarados", "Dragonite", "Onyx"]
print(pokemon)
print()

# Print element at index 2
print("Printing the third Pokemon...")
print(pokemon[2])
print()

# Print elements from index 2 to index 5
print("Printing 3rd Pokemon to the 5th Pokemon...")
print(pokemon[2:5])
print()

# Print elements from index 3 to the end of the list
print("Printing every Pokemon after the first three...")
print(pokemon[3:])
print()

# Print elements from beginning of list to index 3
print("Printing every Pokemon up to the first three...")
print(pokemon[:3])
print()

# Print every other element
print("Printing every other Pokemon")
print(pokemon[::2])
print()

# Print the last element of the list
print("Printing the last Pokemon on the list...")
last_pokemon = pokemon[-1]
print(last_pokemon)
print()

# Find the index of the particular element name
print("Determining the order of Pokemon 'Gyarados'...")
print(pokemon)
print(pokemon.index("Gyarados"))
print()

# Change a specified element within the list at the given index
print("Changing Pokemon name 'Pikachu' to 'Raichu'...")
pokemon[0] = "Raichu"
print(pokemon)
print()

# Add an element to the end of the list
print("Adding a new Pokemon to the end of the list...")
pokemon.append("Magikarp")
print(pokemon)
print()

# Remove an element from the list based on the given element name
print("Removing employee 'Magikarp'...")
pokemon.remove("Magikarp")
print(pokemon)
print()

# Remove an element from the list based on the given index
print("Removing employee 'Bulbasaur' based off of its index")
bulbasaur_index = pokemon.index("Bulbasaur")
pokemon.pop(bulbasaur_index)
print(pokemon)
print()

# Calculate the number of elements within the list
print("Calculating the number of Pokemon...")
print(len(pokemon))
print()
