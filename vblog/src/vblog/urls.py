"""
URL configuration for vblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
import writers.views as writers_views
import posts.views as posts_views
from vblog import settings
# from posts.views import upload_images

urlpatterns = [
    path('', writers_views.WritersList.as_view(), name='index'),

    path('posts/', posts_views.index, name='posts'),
    path('posts/<int:pk>/', posts_views.PostDetail.as_view(), name='post_detail'),

    path('posts/create_post/', posts_views.create_post, name='create_post'),
   # path('upload_images/',upload_images, name = 'image_form' ),

    path('writer/create/', writers_views.WriterCreate.as_view(), name='create_writer'),
    # path('animal/<int:pk>/', animals_views.animal),
    path('writer/<int:pk>/', writers_views.WriterDetail.as_view(), name='writer_detail'),
    # auth
    path('auth/', include('myauth.urls', namespace='myauth')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
