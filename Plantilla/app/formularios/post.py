from django import forms
from ..modelos.post import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('id','author', 'title', 'text')