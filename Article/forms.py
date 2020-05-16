from django import forms
from .models import Article

class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_content']