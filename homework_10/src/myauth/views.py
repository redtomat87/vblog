from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView

# Create your views here.
from django.contrib.auth.decorators import login_required

from writers.models import Writer, WriterProfile

def profile(request):
    # Получаем объект писателя и его профиль из базы данных
    writer = Writer.objects.first()  # Получите писателя, как вам нужно
    writer_profile = WriterProfile.objects.first()  # Получите профиль писателя, как вам нужно

    # Передаем данные в шаблон для отображения
    context = {
        'writer': writer,
        'writer_profile': writer_profile,
    }
    return render(request, 'profile.html', context)

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def logout_view(request):
    logout(request)
    return redirect('/')

class RegisterView(TemplateView):
    template_name = "registration/register.html"


class ProfilePage(TemplateView):
    template_name = "registration/profile.html"