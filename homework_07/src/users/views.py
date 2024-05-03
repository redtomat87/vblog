from django.shortcuts import render
from users.models import User
# Create your views here.

def index(request):
    users_qty = User.objects.count()  # db level -> COUNT()
    users = User.objects.all()

    context = {
        'users': users,
        'users_qty': users_qty,
    }

    return render(request, 'users/index.html', context=context)
