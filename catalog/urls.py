from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('advertisement/<int:pk>', ShowAdvert.as_view(), name='advertisement'),
    path('create_advertisement/', login_required(create_advert), name='create_advertisement'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', user_logout, name='logout'),

]
