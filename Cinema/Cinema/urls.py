from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from UsersApp.views import *
from allauth.account.views import LoginView, LogoutView, SignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('Movies_House.urls')),
    path("Users/", include('UsersApp.urls')),
    path('accounts/', include('allauth.urls'), name='accounts'),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    #path('accounts/profile/', MyMovies, name='profile'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
