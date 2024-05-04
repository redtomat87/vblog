from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from myauth.views import logout_view

app_name = 'myauth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
