"""
These are wikipedia objects.
"""

from django.db import models

# Create your models here.

class Name(models.Model):
    first_name = models.CharField(max_length=10000, blank=True, null=True)
    middle_name = models.CharField(max_length=10000, blank=True, null=True)
    last_name = models.CharField(max_length=10000, blank=True, null=True)
    birth_name = models.CharField(max_length=10000, blank=True, null=True)
    other_names = models.CharField(max_length=10000, blank=True, null=True)
    full_name = models.CharField(max_length=10000, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.middle_name:
            self.full_name = f"{self.first_name} {self.middle_name} {self.last_name}"
        if not self.middle_name:
            self.full_name = f"{self.first_name} {self.last_name}"

        super(Article, self).save(*args, **kwargs)

class Person(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', max_length=10000)
    alt = models.CharField(max_length=10000, blank=True, null=True)
    caption = models.CharField(max_length=10000, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True, )
    birth_place = models.CharField(max_length=10000, blank=True, null=True)
    death_date = models.DateTimeField(blank=True, null=True, )
    death_place = models.CharField(max_length=10000, blank=True, null=True)
    nationality = models.CharField(max_length=10000, blank=True, null=True)
    occupation = models.CharField(max_length=10000, blank=True, null=True)
    years_active = models.CharField(max_length=10000, blank=True, null=True)
    known_for = models.CharField(max_length=10000, blank=True, null=True)
    notable_works = models.CharField(max_length=10000, blank=True, null=True)

    def __str__(self):
        return self.name


    



"""
class Article(models.Model):
    # Article Meta Fields
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=1000, unique=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    category = models.ForeignKey("ArticleCategory", null=True, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, max_length=1000, unique=True)

    def __str__(self):
        return self.title
"""
