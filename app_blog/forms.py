from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={}),
        required=True
    )

    class Meta:
        model = ArticleImage
        fields = '__all__'
