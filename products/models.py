from django.db import models
class Categories(models.Model):
    name=models.CharField('Имя',default='none',max_length=200)
    slug=models.SlugField('Slug',default='none')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'