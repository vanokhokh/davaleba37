from django.urls import path, include
from user.views import Login, Logout, Registration, Userprofile

app_name = 'user'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Registration.as_view(), name='register'),
    path('profile/', Userprofile.as_view(), name='profile'),
]