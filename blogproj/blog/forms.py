from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title','text')

        widgets = {
            # 'author':forms.HiddenInput(initial = user),
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'})
        }

        # def __init__(self, *args, **kwargs):
        #     user = kwargs.pop("user", None)
        #     super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('text','author')

        widgets = {
            'author':forms.HiddenInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'})
        }
