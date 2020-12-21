with open('input') as f:
    cases = [line.rstrip().rstrip(')').split(' (contains ') for line in f.readlines()]

for i in range(0, len(cases)):
    ingredient, allergen = cases[i]
    ingredient = ingredient.split(' ')
    allergen = allergen.split(', ')
    cases[i] = [ingredient, allergen]

allergen_uniques = {}
allergen_count = {}

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

matchings = {}
while True:
    if(allergen_uniques == {}):
        break

    discard_allergens = []
    discard_ingredients = []
    for allergen, value in allergen_uniques.items():
        value = list(value)
        if(len(value) == 1):
            ingredient = value[0]
            matchings[allergen] = ingredient
            discard_allergens.append(allergen)
            discard_ingredients.append(ingredient)

    for discard_allergen in discard_allergens:
        allergen_uniques.pop(discard_allergen)

    for allergen in allergen_uniques:
        for discard_ingredient in discard_ingredients:
            if(discard_ingredient in allergen_uniques[allergen]):
                allergen_uniques[allergen].remove(discard_ingredient)

answers = []
sorted_matchings = sorted(matchings)
for s in sorted_matchings:
    answers.append(matchings[s])
print(','.join(list(answers)))
