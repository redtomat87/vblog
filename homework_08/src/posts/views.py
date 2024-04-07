from django.shortcuts import render

from posts.models import Post


def index(request):
    posts_qty = Post.objects.count() 
    posts = Post.objects.all()
    # animals = Animal.objects.filter(
    #     name__startswith='po',
    #     # age__gte=3,
    # )
    # print(dir(animals))
    # print(animals.query)

    context = {
        'posts': posts,
        'posts count': posts_qty,
    }

    return render(request, 'posts/index.html', context=context)