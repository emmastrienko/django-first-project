from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)
    
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_url_resolves_category_view(self):
        view = resolve('/articles/category/slug')
        self.assertEqual(view.func.view_class, ArticleCategoryList)

    def test_articles_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url_resolves_articles_list_view(self):
        view = resolve('/articles')
        self.assertEqual(view.func.view_class, ArticleList)

    def test_article_detail_view_status_code(self):
        url = reverse('news-detail', args=['2023', '09', '30', 'article-slug'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_article_detail_url_resolves_article_detail_view(self):
        view = resolve('/articles/2023/09/30/article-slug')
        self.assertEqual(view.func.view_class, ArticleDetail)
