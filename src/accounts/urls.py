from django.urls import path
from django.views.generic import TemplateView

from .views import UserLoginView
from .views import UserLogoutView
from .views import UserProfileUpdateView
from .views import UserRegisterView
from .views import user_activate
from .views import user_profile_view

app_name = 'accounts'

urlpatterns = [
    path('registration/activate/<str:sign>/', user_activate, name='register_activate'),
    path('registration/done/',
         TemplateView.as_view(template_name='accounts/user_register_done.html'), name='register_done'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', user_profile_view, name='profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
]
