from django import forms
from courses.models import Course, Category, User, Comment
from teachers.models import Teacher


# class CourseForm(forms.ModelForm):
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-control'}), )
#     teachers = forms.ModelChoiceField(
#         queryset=Teacher.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-control'}), )
#
#     class Meta:
#         model = Course
#         fields = ('title', 'description', 'number_of_students', 'price',
#                   'duration', 'teachers', 'category', 'video',)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password')
        if len(password1) < 2:
            raise forms.ValidationError('Password must be at least 3 characters long.')
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    rating = forms.IntegerField(min_value=1, max_value=5)
    comment = forms.CharField(widget=forms.Textarea)
    if name:
        print(1)
