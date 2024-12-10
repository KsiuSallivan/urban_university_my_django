from django.shortcuts import render


def platform(request):
    return render(request, 'third_task/platform.html')


def games(request):
    items = {
        'Игра 1': 500,
        'Игра 2': 800,
        'Игра 3': 300,
    }
    return render(request, 'third_task/games.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')