from django.shortcuts import render


def group_posts(request, pk):
    template = 'posts/group_list.html'
    return render(request, template)


def index(request):
    template = 'posts/index.html'
    return render(request, template)