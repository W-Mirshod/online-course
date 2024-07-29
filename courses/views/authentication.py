import time
from django.views import View
from django.shortcuts import redirect, render
from courses.forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'others/auth.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user, backend=backend)
            return redirect('index')

        return render(request, 'others/auth.html', {'form': form})


class LogInView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'others/auth.html', {'form': form, 'form_type': 'login'})

    def post(self, request):
        form = LoginForm(request.POST)
        print(form.is_valid())

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user, backend=backend)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password.')
        return render(request, 'others/auth.html', {'form': form, 'form_type': 'login'})


class LogOutView(View):
    def get(self, request):
        logout(request)
        if not request.user.is_authenticated:
            return redirect('index')
        return render(request, 'others/auth.html')


def my_view(request):
    time.sleep(2)
    return render(request, 'others/loading.html')
