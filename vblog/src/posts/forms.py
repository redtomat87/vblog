from django import forms
from .models import Post, Images
from django_prose_editor.fields import ProseEditorFormField


class PostForm(forms.ModelForm):
    tags_input = forms.CharField(max_length=100, label='Tags', required=False)
    body = ProseEditorFormField()

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