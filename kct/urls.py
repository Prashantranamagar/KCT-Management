"""collegemanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from sms import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('list_cord/', views.ListCord.as_view(), name='list_cord'),
    path('add_cord/', views.AddCord.as_view(), name='add_cord'),


    path('update_cord/<int:pk>/', views.UpdateCord.as_view(), name='update_cord'),
    path('detail_cord/<int:pk>/', views.DetailCord.as_view(), name='detail_cord'),
    path('delete_cord/<int:pk>/', views.DelCord.as_view(), name='delete_cord'),


    path('login/',views.LoginView.as_view(), name='login'), 
    path('logout/',views.LogoutView.as_view(), name='logout'), 
    path('register/',views.RegisterView.as_view(), name='register'), 

    path('api/cord_list/', views.APICord.as_view()),

    ]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
