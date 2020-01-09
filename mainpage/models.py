from django.db import models


class Hero(models.Model):
    heading_hero = models.CharField("Название", max_length=250)
    image_hero = models.ImageField("Изображение", upload_to="mainpage/hero", default="", blank=True)

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главные"

    def admin_image(self):
        if self.image_hero:
            from django.utils.safestring import mark_safe
            return mark_safe(
                u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image_hero.url))
        else:
            return '(Нет изображения)'

    admin_image.short_description = 'Изображение'
    admin_image.allow_tags = True


class Services(models.Model):
    name_services = models.CharField("Название", max_length=250)

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"


class Why(models.Model):
    name_why = models.CharField("Название", max_length=150)
    text_why = models.CharField("Описание", max_length=250)

    class Meta:
        verbose_name = "Почему мы?"
        verbose_name_plural = "Почему мы?"


class Work(models.Model):
    image_work = models.ImageField("Фотография", upload_to="mainpage/work", default="", blank=True)
    text_work = models.CharField("Описание", max_length=250)

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работа"

    def admin_image(self):
        if self.image_work:
            from django.utils.safestring import mark_safe
            return mark_safe(
                u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image_work.url))
        else:
            return '(Нет изображения)'

    admin_image.short_description = 'Изображение'
    admin_image.allow_tags = True
