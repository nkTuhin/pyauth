from django.urls import path
from . import views
# from django.contrib.auth import login

urlpatterns = [
    # login urlpatterns
    path('login/', views.login_view, name='login'),
    path('testlogin/', views.test_login_view, name='testlogin'),

    # logout urlpatterns
    path('logined/logout/', views.logout, name='logout'),

    path('register/', views.register_view, name='register'),
    path('register-test/', views.register_test_view, name='register_test'),
]
