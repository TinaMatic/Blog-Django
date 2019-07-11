from django import forms
from blog.models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ('author', 'title', 'image', 'body')

        #widgets connect to the css class
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-group form-control'}),
            'body':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor textarea'})
        }
