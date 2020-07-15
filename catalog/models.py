from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_userforeignkey.models.fields import UserForeignKey
from ckeditor_uploader.fields import RichTextUploadingField


class CarBrand(models.Model):
    ''' Model for the Brand name of a car. '''
    company = models.CharField(max_length=20, verbose_name='Марка машины')

    def __str__(self):
        return self.company

    class Meta:
        ordering = ['company']
        verbose_name = 'Марка машины'
        verbose_name_plural = 'Марки машин'


class BodyType(models.Model):
    ''' Model for the Body type of a car, i.e. coupe, sedan. '''
    body_type = models.CharField(max_length=20, verbose_name='Тип кузова')

    def __str__(self):
        return self.body_type

    class Meta:
        ordering = ['body_type']
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Типы кузова'


class EngineCapacity(models.Model):
    ''' Model for the engine capacity of a car, i.e. 2.5 l.  '''
    engine_capacity = models.FloatField(max_length=20, verbose_name='Литраж')

    def __str__(self):
        return str(self.engine_capacity)

    class Meta:
        ordering = ['engine_capacity']
        verbose_name = 'Литраж'
        verbose_name_plural = 'Литражи'


class Color(models.Model):
    ''' Model for the color of a car. '''
    color = models.CharField(max_length=20, verbose_name='Цвет')

    def __str__(self):
        return self.color

    class Meta:
        ordering = ['color']
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class GearBox(models.Model):
    ''' Model for the Gear box of a car. '''
    gear_box = models.CharField(max_length=20, verbose_name='Коробка передач')

    def __str__(self):
        return self.gear_box

    class Meta:
        ordering = ['gear_box']
        verbose_name = 'Коробка передач'
        verbose_name_plural = 'Коробки передач'


class Drive(models.Model):
    ''' Model for the drive of a car, i.e. front-wheel drive. '''
    drive = models.CharField(max_length=20, verbose_name='Привод')

    def __str__(self):
        return self.drive

    class Meta:
        ordering = ['drive']
        verbose_name = 'Привод'
        verbose_name_plural = 'Приводы'


class Advertisement(models.Model):
    ''' Model of an advertisement made by user (UserForeignKey package used) to sell a car '''
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='Марка машины')
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, verbose_name='Тип кузова')
    gear_box = models.ForeignKey(GearBox, on_delete=models.CASCADE, verbose_name='Коробка передач')
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE, verbose_name='Привод')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет')
    cover_img = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Обложка объявления')
    year = models.IntegerField(verbose_name='Год выпуска')
    mileage = models.IntegerField(verbose_name='Пробег')
    engine_capacity = models.ForeignKey(EngineCapacity, on_delete=models.CASCADE, verbose_name='Литраж')
    description = RichTextUploadingField(verbose_name='Описание')
    seller = UserForeignKey(auto_user_add=True, on_delete=models.CASCADE, verbose_name='Продавец',
                            related_name='advertisement')
    price = models.IntegerField(verbose_name='Цена')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано?')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f"{self.brand}, {self.color}, {self.seller}, {self.price}"

    def get_absolute_url(self):
        return reverse('advertisement', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'
