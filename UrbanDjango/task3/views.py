from django.shortcuts import render

# Create your views here.
def platform(request):
    title = 'Главная страница'
    main = 'Главная'
    market = 'Магазин'
    cart = 'Корзина'
    context = {
        'title': title,
        'main': main,
        'market': market,
        'cart': cart
    }
    return render(request, 'platform.html', context)


def games(request):
    return render(request, 'games.html')


def cart(request):
    return render(request, 'cart.html')