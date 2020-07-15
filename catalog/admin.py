from django.contrib import admin
from catalog.models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Admin Panel action
def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


# Admin Panel action
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)


# Admin Panel action description
make_published.short_description = "Опубликовать выделенные объявления"
make_unpublished.short_description = "Отменить публикацию выделенных объявлений"


# To add CKeditor to the admin page
class AdvertisementAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Advertisement
        fields = "__all__"


# Admin model for advertisement
class AdvertisementAdmin(admin.ModelAdmin):
    form = AdvertisementAdminForm
    save_on_top = True
    save_as = True

    fields = ['brand', 'year', 'body_type', 'color', 'gear_box', 'drive', 'mileage', 'engine_capacity', 'cover_img',
              'description', 'price', 'seller', 'is_published', 'pub_date']
    list_display = ['id', 'brand', 'color', 'gear_box', 'year', 'mileage', 'price', 'seller', 'is_published',
                    'pub_date']
    list_display_links = ['id', 'brand']
    search_fields = ['seller__username', 'seller__email', 'price']
    list_filter = ['brand', 'year', 'gear_box', 'drive', 'is_published']
    readonly_fields = ['seller', 'pub_date']

    actions = [make_published, make_unpublished]


# Registering models to the admin page
admin.site.register(CarBrand)
admin.site.register(BodyType)
admin.site.register(EngineCapacity)
admin.site.register(Color)
admin.site.register(GearBox)
admin.site.register(Drive)
admin.site.register(Advertisement, AdvertisementAdmin)
