from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.


class SignUpView(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class= CustomUserCreationForm


class ChangeAccView(UpdateView):
    model = CustomUser
    template_name = 'change.html'
    succes_url = reverse_lazy('home')
    form_class = CustomUserChangeForm

