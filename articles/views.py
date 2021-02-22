from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin

from django.shortcuts import render
from django.views import generic
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

class ArticleListView(generic.ListView):
    template_name  = 'article_list.html'
    model = Article


class ArticleDetaiView(LoginRequiredMixin, generic.DetailView):
    template_name = 'article_detail.html'
    model = Article
    login_url = 'login'


class ArticleEditView(UserPassesTestMixin, LoginRequiredMixin,generic.UpdateView):
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    model = Article
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user




class ArticleDeleteView(UserPassesTestMixin, LoginRequiredMixin, generic.DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'body',)
    login_url = 'login'

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
