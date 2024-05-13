from django import forms
from .models import Post, Images



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']
        widgets = {
            'author': forms.HiddenInput(),
        }

class ImageForm(forms.ModelForm):

   class Meta:
      model = Images
      fields = ['image_url','image']