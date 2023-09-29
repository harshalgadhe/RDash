from django.urls import path
from authentication import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.login_user, name='login'),
    path('signup', views.signup_user, name='signup'),
    path('authenticate_user', views.authenticate_user, name='authenticate'),
    path('create_user', views.create_user, name='create_user'),
    path('logout', views.logout_user, name='logout')
]