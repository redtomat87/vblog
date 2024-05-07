from django.shortcuts import render, get_object_or_404

from posts.models import Post
from django.views.generic import DetailView, ListView, CreateView


def index(request):
    posts_qty = Post.objects.count() 
    posts = Post.objects.order_by('published_at')

    context = {
        'posts': posts,
        'posts count': posts_qty,
    }

    return render(request, 'posts/index.html', context=context)

def create_post(request):
    posts_qty = Post.objects.count() 
    posts = Post.objects.order_by('published_at')

    context = {
        'posts': posts,
        'posts count': posts_qty,
    }

    return render(request, 'posts/create_post.html', context=context)

class PostsList(ListView):
    page_title = 'Posts'
    model = Post
    paginate_by = 2


class PostCreate(CreateView):
    model = Post
    page_title = 'create_post'
    fields = '__all__'
    # form_class = ...
    # success_url = ...
    success_url = '/'

class PostDetail(DetailView):
    page_title = 'Post page'
    model = Post

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'posts/post_detail.html', {'post': post})
    

    # template_name = 'animals/animal.html'
    # template_name_suffix = '_info'

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs.order_by('-id')
    #     return qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # print(f'{context=}')
    #     context['page_title'] = 'Animal page'
    #
    #     return context
