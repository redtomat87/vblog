from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from myauth.views import logout_view
from myauth.views import RegisterView, ProfilePage

app_name = 'myauth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/', ProfilePage.as_view(), name="profile"),
]
