from catalog.models import *
import django_filters
from django import forms


class AdvertisementFilter(django_filters.FilterSet):
    """ Filtering of advertisements is done by this filter (django_filters package) """

    brand = django_filters.ModelChoiceFilter(empty_label='Выберите Марку', lookup_expr='exact',
                                             queryset=CarBrand.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    body_type = django_filters.ModelChoiceFilter(empty_label='Выберите Тип Кузова', lookup_expr='exact',
                                                 queryset=BodyType.objects.all(),
                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    gear_box = django_filters.ModelChoiceFilter(empty_label='Выберите Коробку Передач', lookup_expr='exact',
                                                queryset=GearBox.objects.all(),
                                                widget=forms.Select(attrs={'class': 'form-control'}))
    drive = django_filters.ModelChoiceFilter(empty_label='Выберите Привод', lookup_expr='exact',
                                             queryset=Drive.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    color = django_filters.ModelChoiceFilter(empty_label='Выберите Цвет', lookup_expr='exact',
                                             queryset=Color.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    year = django_filters.NumberFilter(lookup_expr='lte', label='Год выпуска не позже чем',
                                       widget=forms.NumberInput(
                                           attrs={'class': 'form-control', 'placeholder': 'Введите год'}))
    engine_capacity = django_filters.ModelChoiceFilter(empty_label='Выберите Объем Двигателя',
                                                       label='Объем двигателя не больше чем',
                                                       lookup_expr='lte',
                                                       queryset=EngineCapacity.objects.all(),
                                                       widget=forms.Select(attrs={'class': 'form-control'}))
    mileage = django_filters.NumberFilter(lookup_expr='lte', label='Пробег не больше чем',
                                          widget=forms.NumberInput(
                                              attrs={'class': 'form-control', 'placeholder': 'Введите Пробег'}))
    price = django_filters.NumberFilter(lookup_expr='lte', label='Не дороже чем',
                                        widget=forms.NumberInput(
                                            attrs={'class': 'form-control', 'placeholder': 'Введите Цену'}))

    class Meta:
        model = Advertisement
        fields = ['brand', 'body_type', 'gear_box', 'drive', 'color', 'year', 'mileage', 'engine_capacity', 'price']
