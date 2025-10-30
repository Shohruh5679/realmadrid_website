from django.shortcuts import render
from .models import News, Trophy, Player

def home(request):
    news_list = News.objects.all().order_by('-created_at')  # yangiliklarni ko‘rsatish
    return render(request, 'blog/home.html', {'news_list': news_list})

def trophies(request):
    trophies = Trophy.objects.all().order_by('-year')  # sovrinlar ro‘yxati
    return render(request, 'blog/trophies.html', {'trophies': trophies})

def players(request):
    players = Player.objects.all()  # futbolchilar ro‘yxati
    return render(request, 'blog/players.html', {'players': players})


