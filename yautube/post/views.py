from django.shortcuts import render
from .models import Post


posts = Post.objects.order_by('pub_date')[:10]

context = {'all_posts': posts,
            }


def group_posts(request, pk):
    template = 'posts/group_list.html'
    context['pk'] = pk
    return render(request, template, context)


def index(request):
    template = 'posts/index.html'
    return render(request, template, context)