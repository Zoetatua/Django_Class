from django.db import models

# Create your models here.
class ProjectFormat(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    tech_Tack = models.TextField()
    programmer = models.CharField()
    image = models.ImageField(default='kk.jpg')
    date = models.DateTimeField(auto_now_add=True)
    projectlink = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title