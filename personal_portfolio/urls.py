"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views
import blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('do_something', views.do_something, name='do_something'),
    path('about_me/', views.about_me, name='about_me'),
    path('all_projects/', views.all_projects, name='all_projects')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)