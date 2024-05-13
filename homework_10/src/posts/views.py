from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post, Images
from django.views.generic import DetailView, ListView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.forms import ImageForm, PostForm
from django.http import HttpResponseRedirect


def index(request):
#    posts_qty = Post.objects.count() 
    posts = Post.objects.order_by('published_at')
#    image_url = Images.objects.prefetch_related('post_id').first

    default_page = 1
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', default_page)  # Получаем номер текущей страницы
    try:
        page_posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Если номер страницы не является целым числом, отображаем первую страницу
        page_posts = paginator.page(default_page)
    except EmptyPage:
        # Если номер страницы находится вне диапазона (например, 9999),
        # отображаем последнюю доступную страницу
        page_posts = paginator.page(paginator.num_pages)

    context = {
#        'posts': page_posts,
#        'posts count': posts_qty,
#        'image_url': image_url,
        'page_posts': page_posts,
    }

    return render(request, 'posts/index.html', context=context)

# def create_post(request):
#     posts_qty = Post.objects.count() 
#     posts = Post.objects.order_by('published_at')

#     context = {
#         'posts': posts,
#         'posts count': posts_qty,
#     }

#     return render(request, 'posts/create_post.html', context=context)


class PostsList(ListView):
    page_title = 'Posts'
    model = Post

    def image_detail(request, pk):
        image_url = get_object_or_404(Images, pk=pk)
        return render(request, 'posts/index.html', {'image_url': image_url})

# class PostCreate(CreateView):
#     model = Post
#     page_title = 'create_post'
#     fields = '__all__'
#     # form_class = ...
#     # success_url = ...
#     success_url = '/'
    

class PostDetail(DetailView):
    page_title = 'Post page'
    model = Post

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'posts/post_detail.html', {'post': post})

@login_required
def create_post(request):
    print(request.user.id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, initial = {'post_form.author':request.user.id})
        image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)  
            post.author = request.user
            post.save() 
            image = image_form.save(commit=False)
    #        image.post = post
            image.save()
            return redirect('posts/index.html')
    else:
        post_form = PostForm()
        image_form = ImageForm()
    return render(request, 'posts/post_form.html', {'post_form': post_form, 'image_form': image_form})


# def upload_images(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/") 
#     else:
#         form = ImageForm()

#     return render(request, 'posts/image_form.html', {'form':form})