from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """ Класс модели обратной связи """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Форма обратной связи'

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """ Класс модели контактов """
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Настройка ссылок в контактах'
        verbose_name_plural = 'Настройка ссылок в контактах'

    def __str__(self):
        return self.name


class About(models.Model):
    """ Класс модели страницы о нас """
    name = models.CharField(max_length=50, default='')
    text = RichTextField()
    mini_text = RichTextField()

    class Meta:
        verbose_name = 'Настройка страницы о нас'
        verbose_name_plural = 'Настройка страницы о нас'

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        return self.about_images.order_by('id')[1:]

    def __str__(self):
        return self.name


class ImageAbout(models.Model):
    """ Класс модели изображений страницы о нас """
    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(About,
                             on_delete=models.CASCADE,
                             related_name='about_images')
    alt = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Настройка изображений страницы о нас'
        verbose_name_plural = 'Настройка изображений страницы о нас'


class Social(models.Model):
    """ Класс модели соц сетей страницы о нас """
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField()

    class Meta:
        verbose_name = 'Настройка ссылок-соц сетей страницы о нас'
        verbose_name_plural = 'Настройка ссылок-соц сетей страницы о нас'

    def __str__(self):
        return self.name
