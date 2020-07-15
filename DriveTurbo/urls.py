from django.contrib import admin
from django.urls import path, include
from DriveTurbo import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('catalog.urls')),  #Catalog/urls.py

]


# SETTINGS FOR DEBUGGING
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
