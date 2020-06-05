from blog.models import Comment,Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text')
        widget={
            'title':forms.TextInput(attrs={'class':'textInputClass'}),
            'text':forms.Textarea(attrs={'class':'medium-editor-textarea editable postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']
        widget={
            'text':forms.Textarea(attrs={'class':'medium-editor-textarea editable'})
        }
