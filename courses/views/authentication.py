from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.views import View
from courses.forms import SignUpForm, LoginForm


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'auth.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        print(form.is_valid())

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

        return render(request, 'auth.html', {'form': form})


class LogInView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth.html', {'form': form, 'form_type': 'login'})

    def post(self, request):
        form = LoginForm(request.POST)
        print(form.is_valid())

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password.')
        return render(request, 'auth.html', {'form': form, 'form_type': 'login'})
