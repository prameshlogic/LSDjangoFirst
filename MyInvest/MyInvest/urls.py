"""
URL configuration for MyInvest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from investApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('investApp.urls')),
    path('', views.hmpage,name="hmpage"),
    path('login/',views.lgpage,name="login"),
    path('sg/',views.signup,name="sg"),
    path('lg/', views.login,name="lg"),
    path('signup/', views.signpage,name="sign"),
    path('profileEdit/<int:pk>',views.profileEdit,name="profileEdit"),
    path('profileCreate/', views.profileCreate,name="profileCreate"),
    path('profileDelete/<int:pk>/', views.profileDelete,name="profileDelete"),
    path('pramesh', views.userLogout,name="userLogout"),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


