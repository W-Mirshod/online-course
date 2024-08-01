from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View
from courses.forms import SignUpForm


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'auth.html', {'form': form})

    def post(self, request):
        print(1)
        form = SignUpForm(request.POST)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            print(2)
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(request, 'auth.html', {'form': form})
