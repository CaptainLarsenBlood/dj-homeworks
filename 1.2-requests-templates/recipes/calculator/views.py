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


def get_recipes(request, food):
    servings = int(request.GET.get('servings', 1))
    new_amount = {}
    for key in DATA[food]:
        new_amount[key] = DATA[food][key]*servings
    return render(request, 'calculator/index.html', context={'recipe': new_amount, 'food': food})


