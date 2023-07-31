from django import forms
from media_land.common.models import Comment, Search


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'placeholder': 'Add comment here ...',
            })
        }


class SearchForm(forms.ModelForm):
    search_text = forms.CharField(label="", help_text="", required=False,
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Search in page...',
                                        }))

    class Meta:
        model = Search
        fields = ['search_text']
