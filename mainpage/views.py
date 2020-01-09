from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.views.generic.base import View

from .forms import UserLoginForm, UserRegistrationForm
from .models import Hero
from .models import Services
from .models import Why
from .models import Work


class HeroView(View):
    def get(self, request):
        hero_section = Hero.objects.all()
        services_section = Services.objects.all()
        why_section = Why.objects.all()
        work_section = Work.objects.all()
        return render(request, "pages/mainpage_list.html",
                      {
                          "hero_list": hero_section,
                          "services_list": services_section,
                          "why_list": why_section,
                          "work_list": work_section,
                      })


def login_view(request):
    form = UserLoginForm(request.POST or None)
    next_ = request.GET.get('next')
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username.strip(),
                            password=password.strip())
        login(request, user)
        next_post = request.POST.get('next')
        rederict_path = next_ or next_post or 'dashboard'
        return redirect(rederict_path)
    return render(request, 'pages/login_page.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'pages/edit_profile.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'pages/register_page.html', {'form': user_form})


@login_required
def dashboard_view(request):
    return render(request, "pages/admin_app.html")
