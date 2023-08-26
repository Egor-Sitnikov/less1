from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisements
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements}
    return render(request, "app_advertisements/index.html", context)

def top_sellers(request):
    return render(request, "app_advertisements/top-sellers.html")

@login_required(login_url=reverse_lazy('login'))
def advertisements_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)



# def sign_up(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         return render(request, 'users/register.html', {'form': form})


# class RegisterView(FormView):
#     form_class = RegisterForm
#     template_name = 'app_auth/register.html'
#     success_url = reverse_lazy('app_lesson_4/index.html')
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
