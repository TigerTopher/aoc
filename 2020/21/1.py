with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

for i in range(0, len(cases)):
    ing, allergen = cases[i].rstrip(')').split(' (contains ')
    ing = ing.split(' ')
    allergen = allergen.split(', ')
    cases[i] = [ing, allergen]

possible_ing = {}
ingredient_count = {}
allergen_count = {}

for i in range(0, len(cases)):
    ingredients = cases[i][0]
    allergens = cases[i][1]

    for allergen in allergens:
        for ingredient in ingredients:
            if (not ingredient in possible_ing):
                possible_ing[ingredient] = {}
                possible_ing[ingredient][allergen] = 1
            elif (not allergen in possible_ing[ingredient]):
                possible_ing[ingredient][allergen] = 1
            else:
                possible_ing[ingredient][allergen] += 1

        if (not allergen in allergen_count):
            allergen_count[allergen] = 1
        else:
            allergen_count[allergen] += 1

    for ingredient in ingredients:
        if (not ingredient in ingredient_count):
            ingredient_count[ingredient] = 1
        else:
            ingredient_count[ingredient] += 1

possible = set()

for allergen, count in allergen_count.items():
    for ingredient, allergens in possible_ing.items():
        if allergen in allergens and allergens[allergen] == count:
            possible.add(ingredient)

total_count = 0
for ingredient, count in ingredient_count.items():
    if not ingredient in possible:
        total_count += count

print(total_count)
