lemon_recipe = {"3_cups": "all_purpose_flour", "2_1/2": "baking powder", "1/2_teaspoon": "baking_soda", "1/2_teaspoon": "salt", "1_cup": "unsalted_butter", "1_3/4_cups": "granulated_sugar",
               "3": "large_eggs", "2_teaspoon": "vanilla_extract", "1_cup": "milk", "1_tablespoon": "lemon_zest", "1/3_cup": "lemon_juice"}

redvelvet_recipe = {"3_cups": "cake_flour", "1_teaspoon": "baking_soda", "2_Tablespoons": "cocoa_powder", "1/2_teaspoon": "salt", "1/2_cup": "unsalted_butter", "2_cups": "granulated_sugar",
                   "1_cup": "vegetable_oil", "4": "large_eggs", "1_Tablespoon": "vanilla_extract", "1_teaspoon": "white_vinegar", "1": "red_food_coloring", "1_cup": "buttermilk"}



def similar_ingredients(recipe1, recipe2):
    similar_ingredients = []
    for ingredient1 in recipe1.values():
        if ingredient1 in recipe2.values():
            similar_ingredients.append(ingredient1)
    return similar_ingredients

similar_ingredients = similar_ingredients(lemon_recipe, redvelvet_recipe)
print("Similar ingredients:", similar_ingredients)
