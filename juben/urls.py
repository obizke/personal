from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from juben import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('details/<str:pk>/', views.details, name='details'),
    path('results/', views.results, name='results'),
    path('blog/', views.blog, name='blog'),
    path('product/', views.product, name='product'),
    path('product_details/<str:pk>/', views.product_details, name='product_details')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
