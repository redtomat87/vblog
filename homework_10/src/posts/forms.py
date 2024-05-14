from django import forms
from .models import Post, Images



class PostForm(forms.ModelForm):
    tags_input = forms.CharField(max_length=100, label='Tags', required=False)

    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'author': forms.HiddenInput(),
        }

class ImageForm(forms.ModelForm):

   class Meta:
      model = Images
      fields = ['image_url','image']
      widgets = {
            'post': forms.HiddenInput(),
          }      