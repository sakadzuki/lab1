import json

# dead_inside - список покемонов
dead_inside_length = 0
dead_inside_signs = 0

#сначала пройдемся по каждой строке файла
with open('pokemon_full.json', 'r') as file:
    for current_line in file:
        if current_line.isalpha() == False: # если в строке есть не только буквы, то пройдемся по каждому символу
            for current_symbol in current_line:
                if current_symbol.isalpha() == False:
                    dead_inside_signs += 1
        dead_inside_length += len(current_line)
file.close()

longest_description = 0
name_longest_description = ""
name_abilitie = ""

with open("pokemon_full.json", "r") as file:
    dead_inside = json.load(file)
    count = 0
    for current_pokemon in dead_inside:
        current_name = current_pokemon['name']
        current_abilities = current_pokemon['abilities']
        current_description = current_pokemon['description']
        if len(current_description) > longest_description:
            longest_description = len(current_description)
            name_longest_description = current_name
        for abilka in current_abilities:
            current_count = 0
            for i in range(0, len(abilka) - 1):
                if (abilka[i] == " " and abilka[i + 1] != " "):
                    current_count += 1
            if current_count > count:
                count = current_count
                name_abilitie = abilka
file.close()

print(dead_inside_length)
print(dead_inside_length - dead_inside_signs)
print(name_longest_description)
print(name_abilitie)