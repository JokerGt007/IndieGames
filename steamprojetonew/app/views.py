from django.shortcuts import render, get_object_or_404
from .models import Game, Discount
from django.utils.timezone import now

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def recent_releases(request):
    from django.utils.timezone import now
    from datetime import timedelta
    one_week_ago = now() - timedelta(days=7)
    recent_games = Game.objects.filter(release_date__gte=one_week_ago.date())
    return render(request, 'games/game_list.html', {'games': recent_games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    
    # Inicialize os valores para preços e descontos
    original_price = game.price
    discounted_price = original_price
    discount_percentage = None
    
    # Verifique se há um desconto ativo para o jogo
    today = now().date()
    active_discounts = Discount.objects.filter(game=game, start_date__lte=today, end_date__gte=today)
    if active_discounts.exists():
        discount = active_discounts.first()  # Supondo que há apenas um desconto ativo por jogo
        discount_percentage = discount.discount_percentage
        discount_amount = (original_price * discount_percentage) / 100
        discounted_price = original_price - discount_amount
    
    context = {
        'game': game,
        'discounted_price': discounted_price,
        'discount_percentage': discount_percentage,
        'original_price': original_price,
    }
    return render(request, 'games/game_detail.html', context)
