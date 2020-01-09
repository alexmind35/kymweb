from django.contrib import admin

from .models import Hero, Services, Why, Work


@admin.register(Hero)
class AdminHero(admin.ModelAdmin):
    list_display = ["heading_hero", "admin_image"]


@admin.register(Services)
class AdminServices(admin.ModelAdmin):
    list_display = ["name_services"]


@admin.register(Why)
class AdminWhy(admin.ModelAdmin):
    list_display = ["name_why", "text_why"]


@admin.register(Work)
class AdminWork(admin.ModelAdmin):
    list_display = ["admin_image", "text_work"]
