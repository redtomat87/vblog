from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def logout_view(request):
    logout(request)
    return redirect('/')

