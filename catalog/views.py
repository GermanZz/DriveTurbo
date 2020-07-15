from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, AdvertForm
from .filters import AdvertisementFilter
from django_filters.views import FilterView
from .models import Advertisement


def url_resolver(request_GET):
    '''URL resolver for paginaton of filtered result'''
    url = []
    for element, pk in request_GET.items():
        if element != 'page':
            url.append(f"{element}={pk}")
    return '&'.join(url)


# Home page with filter
class HomePage(FilterView):
    model = Advertisement
    template_name = 'catalog/index.html'
    context_object_name = 'advertisements'
    paginate_by = 4
    filterset_class = AdvertisementFilter
    queryset = Advertisement.objects.filter(is_published=True).select_related('brand')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = f"{url_resolver(self.request.GET)}&"
        return context


# View to show a single advertisement
class ShowAdvert(DetailView):
    queryset = Advertisement.objects.select_related('seller')
    template_name = 'catalog/single.html'
    context_object_name = 'advertisement'


# View to create advertisement
def create_advert(request):
    if request.method == 'POST':
        form = AdvertForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.success(request, 'Ваше объявление успешно отправлено на рассмотреине. Спасибо!')
            form.save()
            return redirect('home')
    else:
        form = AdvertForm()
    return render(request, 'catalog/add_advertisement.html', {'form': form})


# View for registration
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'catalog/register.html', {'form': form})


# View for login
def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно авторизировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при авторизации!')
    else:
        form = UserLoginForm()
    return render(request, 'catalog/login.html', {'form': form})


# Logout view
def user_logout(request):
    logout(request)
    return redirect('home')
