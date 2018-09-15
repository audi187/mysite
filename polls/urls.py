from django.urls import path

from . import views
app_name="polls"

urlpatterns = [
    path('', views.index, name='index'),
    path('reg/',views.registration, name='register'),
    path('login/',views.login,name='login'),
    path('forghome/',views.ForgHome,name='ForgHome')

]