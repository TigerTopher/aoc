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

matchings = {} # Allergen: Ingredients

while True:
    if(allergen_count == {}):
        break

    pop_allergens = []
    pop_ingredient = []
    for allergen, count in allergen_count.items():
        candidates = []
        for ingredient, allergens in possible_ing.items():
            if allergen in allergens and allergens[allergen] == count:
                candidates.append(ingredient)

        if(len(candidates) == 1):
            matchings[allergen] = candidates[0]
            pop_allergens.append(allergen)
            pop_ingredient.append(candidates[0])
            break
    
    for allergen in pop_allergens:
        allergen_count.pop(allergen)
    for ingredient in pop_ingredient:
        possible_ing.pop(ingredient)

answers = []
sorted_matchings = sorted(matchings)
for s in sorted_matchings:
    answers.append(matchings[s])
print(','.join(list(answers)))

