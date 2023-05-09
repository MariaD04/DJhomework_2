from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipes_view(request, recipe):
    servings = int(request.GET.get('servings', 1))
    recipe_dict = DATA.get(recipe)
    if recipe_dict:
        recipe_keys = list(recipe_dict.keys())
        recipe_values = list(recipe_dict.values()) 
        recipe_values = [i*servings for i in recipe_values]
        ingredients = dict(zip(recipe_keys,recipe_values ))
    else:
        ingredients = dict()
 
    context = {
    'recipe': recipe,
    'ingredients' : ingredients
    }
    return render(request, 'calculator/index.html', context)




    

