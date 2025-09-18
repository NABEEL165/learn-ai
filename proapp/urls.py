"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('adminlogin/', views.adminlogin, name='admin_login'),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
 path('users/', views.user_list, name='user_list'),
path('aiproject/', views.aiprojeect, name='aiproject'),
    path('', views.index, name='index'),
    path('ai/', views.ai, name='ai'),
    path('mechine/', views.mechine, name='mechine'),
    path('deep/', views.deep, name='deep'),
     path("register/", views.register_view, name="register"),
path("login/", views.login_view, name="login"),
    path("guidence/", views.guidence, name="guidence"),
    #  path("dashbord/", views.dashbord, name="dashbord"),
        path("expert/", views.expert_view, name="expert"),

        path("save_contact/", views.save_contact, name="save_contact"),
    path("contact_list/", views.contact_list, name="contact_list")
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
