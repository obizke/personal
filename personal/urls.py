"""personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from project import views
from juben import views as pd

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('juben.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', views.admin, name='admin'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('delete_contact/<str:pk>/', views.delete_contact, name='delete_contact'),
    path('search/', views.search, name='search'),
    path('delete_user/<str:pk>/', views.delete_user, name='delete_user'),
    path('post/', views.post, name='post'),
    path('author/', views.author, name='author'),
    path('update_post/<str:pk>/', views.update_post, name='update_post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete_post'),
    #     products
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<str:pk>/', views.update_product, name='update_product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product'),

]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    