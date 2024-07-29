from django import forms


class CommentForm(forms.Form):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(attrs={'class': 'form-control border-0'}))
    comment = forms.CharField(widget=forms.Textarea)
    media_file = forms.FileField(required=False)
