from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DateDetailView

from .models import Article, Category

# Create your views here.
class HomePageView(TemplateView):
  model = Article
  template_name = 'index.html'
  context_object_name = 'categories'
  def get_context_data(self, **kwargs):
    context = super(HomePageView, 
                    self).get_context_data(**kwargs)
    context['articles'] =\
      Article.objects.filter(main_page=True)[:5]
    return context
  def get_queryset(self, *args, **kwargs):
    categories = Category.objects.all()
    return categories

  
class ArticleDetail(DateDetailView):
  model = Article
  template_name = 'article_detail.html'
  context_object_name = 'item'
  date_field = 'pub_date'
  query_pk_and_slug = True
  month_format = '%m'
  allow_future = True

  def get_context_data(self, *args, **kwargs):
    context = super(ArticleDetail,
                    self).get_context_data(*args, **kwargs)
    try:
      context['images'] = context['item'].images.all()
    except:
      pass

    return context
    
class ArticleList(ListView):
  model = Article
  template_name = 'articles_list.html'
  context_object_name = 'items'

  def get_context_data(self, *args, **kwargs):
    context = super(ArticleList,
                    self).get_context_data(*args, **kwargs)
    try:
      context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))

    except Exception:
      context['category'] = None

    return context
  
  def get_queryset(self, *args, **kwargs):
    articles = Article.objects.all()
    return articles
  

class ArticleCategoryList(ArticleList):
  def get_queryset(self, *args, **kwargs):
    articles = Article.objects.filter(
      category__slug__in=[self.kwargs['slug']]
    ).distinct()
    return articles