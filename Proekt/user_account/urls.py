from django.urls import path
from django.contrib.auth import views as authViews
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.LoginForm, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout/', authViews.LogoutView.as_view(next_page='login'), name='logout'),
    path('courses', views.courses, name='courses')
]