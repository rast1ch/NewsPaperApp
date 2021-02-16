from django.shortcuts import render
from django.views import generic
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

class ArticleListView(generic.ListView):
    template_name  = 'article_list.html'
    model = Article


class ArticleDetaiView(generic.DetailView):
    template_name = 'article_detail.html'
    model = Article


class ArticleEditView(generic.UpdateView):
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    model = Article


class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(generic.CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'body', 'author',)
    
