from django.urls import path
from .views import login_user, logout_user, profile_view, register_user


app_name='accounts'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('log-out/', logout_user, name='log-out'),
    path('register/', register_user, name='register'),
    path('me/', profile_view, name='me'),
]
