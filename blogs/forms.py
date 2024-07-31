from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    rating = forms.IntegerField(min_value=1, max_value=5)
    comment = forms.CharField(widget=forms.Textarea)
    media_file = forms.FileField(required=False)
