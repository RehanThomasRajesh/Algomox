# social_media_dashboard/urls.py
from django.urls import path
from .views import dashboard, get_chart_data, login, signup

urlpatterns = [
    path('', login, name='custom_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('get_chart_data/', get_chart_data, name='get_chart_data'),
    path('user-signup/', signup, name='user_signup'),
    # Add other URL patterns if needed
]
