from django.shortcuts import render
from django.http import HttpResponse



all_grops = [f'grop {i}' for i in range(100)] 


def group_posts(request, pk):
    return HttpResponse(f'group {pk}')


def index(request):
    template = 'posts/index.html'
    return render(request, template)