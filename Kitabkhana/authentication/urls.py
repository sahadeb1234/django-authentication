from django.contrib import admin, auth
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls.conf import include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index page'),
    path('customerregistration/', views.customerregistration, name="customerregistration"),
    path('login/', views.userlogin, name="login"),
    # path('logout/', views.logout, name="logout"),
    path('profil/', views.profil, name="profil"),
    path('change/', views. passwordchange, name="change"),
    path('logout/', auth_views.LogoutView.as_view(next_page= '/'),name="logout")
    # path('logout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'),
    #      name='user-logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
