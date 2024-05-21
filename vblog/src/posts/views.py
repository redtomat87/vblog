from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post, Images, Tags
from django.views.generic import DetailView, ListView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.forms import ImageForm, PostForm
from django.http import HttpResponseRedirect


def index(request):
    posts = Post.objects.order_by('-published_at')

    default_page = 1
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', default_page)  
    try:
        page_posts = paginator.page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(default_page)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    context = {
        'page_posts': page_posts,
    }

    return render(request, 'posts/index.html', context=context)


class PostsList(ListView):
    page_title = 'Posts'
    model = Post

    def image_detail(request, pk):
        image_url = get_object_or_404(Images, pk=pk)
        return render(request, 'posts/index.html', {'image_url': image_url})
    

class PostDetail(DetailView):
    page_title = 'Post page'
    model = Post

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'posts/post_detail.html', {'post': post})

@login_required
def create_post(request):

    if request.method == 'POST':
        post_form = PostForm(request.POST, initial = {'post_form.author':request.user.id})
        image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)  
            post.author = request.user
            post.save() 
            print(post.id)

            tags_input = post_form.cleaned_data.get('tags_input', '')
            tags_list = [tag.strip().lower() for tag in tags_input.split(',')] 

            for tag_name in tags_list:
                tag, created = Tags.objects.get_or_create(name=tag_name)
                post.tags.add(tag)
            
            image = image_form.save(commit=False)
            image.post = post
            image.save()
            return redirect('posts')
    else:
        post_form = PostForm()
        image_form = ImageForm()
    return render(request, 'posts/post_form.html', {'post_form': post_form, 'image_form': image_form})
