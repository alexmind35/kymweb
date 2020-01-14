from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View

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

@login_required
def dashboard_view(request):
    messages.success(request, ('Авторизуйтесь!Введите логин и пароль'))
    return render(request, "pages/admin_page.html")

def logout_user(request):
    logout(request)
    return redirect('home')
