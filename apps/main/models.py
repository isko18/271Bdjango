from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип"
    )
    banner = models.ImageField(
        upload_to='banner',
        verbose_name="Баннер"
    )
    facebook = models.URLField(
        verbose_name="facebook"
    )
    twitter = models.URLField(
        verbose_name="twitter"
    )
    google = models.URLField(
        verbose_name="google"
    )
    linkedin = models.URLField(
        verbose_name="linkedin"
    )    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"