from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('free', views.free, name='free'),
    path('tou', views.tou, name='tou'),
    path('mothpay', views.mothpay, name='mothpay'),
    path('moth', views.mothcheck, name='moth'),
    path('yearpay', views.yearpay, name='yearpay'),
    path('year', views.yearcheck, name='year'),
    path('reject', views.reject, name="reject"),
    path('balance', views.balance, name="balance"),
    path('balancepay', views.balancepay, name="balancepay"),
    path('balancecheck', views.balancecheck, name="balancecheck"),
]