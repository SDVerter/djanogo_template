from django.db import models

# Create your models here.


from markdownx.models import MarkdownxField

class Page(models.Model):
    autoshowadmin =True
    slug=models.TextField(blank=False)
    Page= MarkdownxField()
    
    def __str__(self):
        return self.slug
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"