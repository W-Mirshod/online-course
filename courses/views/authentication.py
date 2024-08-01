from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from courses.forms import SignUpForm

from django.views.generic import CreateView


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'auth.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
