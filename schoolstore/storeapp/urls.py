from . import views
from django.urls import path

app_name='storeapp'
urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('content/',views.content,name='content'),
    path('form/',views.form,name='form')
]