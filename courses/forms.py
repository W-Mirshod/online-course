from django import forms
from courses.models import Course, Category
from teachers.models import Teacher


class CourseForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}), )
    teachers = forms.ModelChoiceField(
        queryset=Teacher.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}), )

    class Meta:
        model = Course
        fields = ('title', 'description', 'number_of_students', 'price',
                  'duration', 'teachers', 'category', 'video',)
