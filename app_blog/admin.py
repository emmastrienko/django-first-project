from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.urls import path, include
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('app_blog.urls')),
]
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('category',)
  fieldsets = [
    (None, {
      'fields': ['category']
    })
  ]
admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
  model = ArticleImage
  form = ArticleImageForm
  extra = 0

  fieldsets = (
    ('', {
      'fields': ('title', 'image',),
    }),
  )

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'pub_date', 'slug', 'main_page')
  inlines = [ArticleImageInline]
  multiload_form = True
  multiload_list = False
  prepopulated_fields = {'slug': ('title',)}
  raw_id_fields = ('category',)
  fieldsets = (
    ('', {
        'fields': ('pub_date', 'title', 'description', 'main_page'),
    }),
    ((u'Додатково'), {
        'classes': ('grp-collapse grp-closed',),
        'fields': ('slug',),
    }),
  )

  def delete_file(self, pk, request):
      '''Delete on image.'''

      obj = get_object_or_404(ArticleImage, pk=pk)
      return obj.delete()
    
admin.site.register(Article, ArticleAdmin)
