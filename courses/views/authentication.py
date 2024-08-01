import uuid
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from courses.forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout

from courses.models import Profile


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


class SignUpView(CreateView):
    template_name = "others/auth.html"
    form_class = SignUpForm
    success_url = "/courses/home/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        Profile.objects.get_or_create(user=user)

        profile = user.profile
        profile.activation_token = str(uuid.uuid4())
        profile.save()

        form.send_email(user)
        return super().form_valid(form)


class ActivateView(View):
    def get(self, request, token):
        profile = get_object_or_404(Profile, activation_token=token)
        user = profile.user
        user.is_active = True
        user.save()
        profile.delete()
        user.backend = "django.contrib.auth.backends.ModelBackend"
        login(request, user, backend=user.backend)
        login(request, user)
        return redirect('index')


class LogOutView(View):
    def get(self, request):
        logout(request)
        if not request.user.is_authenticated:
            return redirect('index')
        return render(request, 'others/auth.html')


class GoToHomeView(View):
    def get(self, request):
        return render(request, 'others/glowing button.html')
