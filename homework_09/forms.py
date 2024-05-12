from django import forms
from ..homework_10.src.posts.models import Post
from django.forms.widgets import FileInput
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget

class MultipleFileInput(FileInput):
    allow_multiple_selected = True

    def render(self, name, value, attrs=None, renderer=None):
        attrs['multiple'] = 'multiple'
        return super().render(name, value, attrs, renderer)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        return [files.get(name)]

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'images': MultipleFileInput(attrs={'multiple': True}),  # Use the custom widget
        }