from django.urls import path
from . import views


# The app name 

app_name = "accounts"

# URL patterns

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]
