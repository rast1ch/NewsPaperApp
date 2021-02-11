from django.urls import path
from django.contrib.auth import views

from .views import SignUpView, ChangeAccView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
   # path('change/', ChangeAccView.as_view(), name = 'change')
]
