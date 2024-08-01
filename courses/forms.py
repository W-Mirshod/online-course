from django import forms
from django.core.mail import send_mail

from courses.models import Course, Category, User, Comment, BoughtCourse, ContactMessage
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

    def send_email(self, user):
        token = user.profile.activation_token
        activation_link = f"http://127.0.0.1:8000/courses/activate/{token}"

        send_mail(
            subject="Account Activation",
            message=f"Please click the following link to activate your account: {activation_link}",
            from_email='W Man',
            recipient_list=[user.email],
            fail_silently=False,
        )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


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


class GettingCoursesForm(forms.ModelForm):
    class Meta:
        model = BoughtCourse
        fields = ('name', 'course_id',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
