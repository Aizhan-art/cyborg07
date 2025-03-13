from django.urls import path
from . import views
from .views import toggle_2fa




urlpatterns = [
    path('register/', views.user_register_view, name='register'),
    path('login/', views.user_login_view, name='login'),
    path('logout/', views.user_logout_view, name='logout'),

    path('otp_verify/<int:user_id>/', views.otp_verification_view, name='otp_verify'),

    path('toggle-2fa/',toggle_2fa, name='toggle_2fa')
]
