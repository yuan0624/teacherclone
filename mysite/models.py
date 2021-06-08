from django.db import models
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Country(models.Model):
	name = models.CharField(max_length=10)
	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=10)
	population = models.PositiveIntegerField(default=0)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	def __str__(self):
		return self.name