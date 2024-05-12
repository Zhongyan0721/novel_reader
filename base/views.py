from django.shortcuts import render
from django.http import HttpResponse
from .models import Novel


# books = [
#             {'id': 1, 'name': 'Novel_0'},
#             {'id': 2, 'name': 'Novel_1'}
#         ]

def home(request):
    novels = Novel.objects.all()
    context = {
        'novel': novels,
    }
    return render(request, 'home.html', context)

def novel(request, id):
    novel = Novel.objects.get(id=id)
    context = {
        'novel': novel
    }
    return render(request, 'novel.html', context)