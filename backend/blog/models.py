from django.db import models
from datetime import datetime
from django.db.models.query import QuerySet
from django.template.defaultfilters import slugify


class Escolhas(models.TextChoices):
    GERAL = 'geral'
    ACESSIBILIDADE = 'acessibilidade'
    COMPORTAMENTO = 'comportamento'
    INOVAÇÃO = 'inovação'
    ENSAIO = 'ensaio'
    DESIGN = 'design'
    

class PostBlog(models.Model):
    titulo: models.CharField(max_length=70)
    slug: models.SlugField()
    categoria: models.CharField(max_length=70, choices=Escolhas.choices, default=Escolhas.GERAL)
    thumbnail: models.ImageField(upload_to='photos/%d/%m/%Y')
    chamada = models.CharField(max_length=150)
    mês = models.CharField(max_length=3)
    dia = models.CharField(max_length=2)
    conteúdo = models.TextField()
    feature = models.BooleanField(default=False)
    data_criação = models.DateTimeField(default=datetime.now, blank=True)

#Atualizar slug automaticamente
    def save(self, *args, **kwargs):
        slug_original = slugify(self.título)
        queryset = PostBlog.objects.all().filter(slug__iexact=slug_original).count()

#Loop para se certificar que ao achar slugs iguais, continuar até que não reste nenhumm
        count = 1
        slug = slug_original
        while(queryset):
            slug = slug_original + '-' + str(count)
            count += 1
            queryset = PostBlog.objects.all().filter(slug__iexact=slug).count()
        self.slug = slug

        if self.feature:
            try:
                temp = PostBlog.objects.get(feature=True)
                if self != temp:
                    temp.feature = False
                    temp.save
            except PostBlog.DoesNotExist:
                pass

        super(PostBlog, self).save(*args, **kwargs)

    def __str__(self):
        return self.título