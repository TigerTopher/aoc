with open('input') as f:
    cases = [line.rstrip().rstrip(')').split(' (contains ') for line in f.readlines()]

for i in range(0, len(cases)):
    ingredient, allergen = cases[i]
    ingredient = ingredient.split(' ')
    allergen = allergen.split(', ')
    cases[i] = [ingredient, allergen]

allergen_uniques = {}
allergen_count = {}
ingredient_count = {}

for case in cases:
    ingredients = case[0]
    allergens = case[1]
    for allergen in allergens:
        if (not allergen in allergen_uniques.keys()):
            allergen_uniques[allergen] = set(ingredients)
        else:
            allergen_uniques[allergen] = set.intersection(allergen_uniques[allergen], ingredients)
        if (not allergen in allergen_count):
            allergen_count[allergen] = 0
        allergen_count[allergen] += 1
    for ingredient in ingredients:
        if (not ingredient in ingredient_count):
            ingredient_count[ingredient] = 0
        ingredient_count[ingredient] += 1

possible_ingredients = set()
for allergen in allergen_uniques:
    possible_ingredients = set.union(allergen_uniques[allergen], possible_ingredients)

total_count = 0
for ingredient in ingredient_count:
    if not ingredient in possible_ingredients:
        total_count += ingredient_count[ingredient]

print(total_count)
